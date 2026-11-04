const API = "/api";

// Show selected section
function showSection(id) {
    document.querySelectorAll(".section").forEach(function(section) {
        section.classList.add("hidden");
    });

    document.getElementById(id).classList.remove("hidden");

    if (id === "dashboard") loadDashboard();
    if (id === "animals") loadAnimals();
    if (id === "alerts") loadAlerts();
}

// Load dashboard information
async function loadDashboard() {
    try {
        const response = await fetch(API + "/dashboard");
        const data = await response.json();

        document.getElementById("totalAnimals").textContent = data.total_animals;
        document.getElementById("totalAlerts").textContent = data.new_alerts;
        document.getElementById("totalVaccinations").textContent = data.total_vaccinations;
    } catch (error) {
        alert("Dashboard loading failed. Check backend.");
    }
}

// Load animals
async function loadAnimals() {
    try {
        const response = await fetch(API + "/animals");
        const animals = await response.json();

        let output = "";

        animals.forEach(function(animal) {
            output += "<div class='item'>";
            output += "ID: " + animal.id;
            output += " | Tag: " + animal.tag;
            output += " | Species: " + animal.species;
            output += " | Breed: " + (animal.breed || "-");
            output += " | Age: " + (animal.age || "-");
            output += "</div>";
        });

        if (output === "") {
            output = "No animals registered yet.";
        }

        document.getElementById("animalList").innerHTML = output;

    } catch (error) {
        alert("Unable to load animals.");
    }
}

// Register animal
document.getElementById("animalForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const animal = {
        tag: document.getElementById("tag").value,
        species: document.getElementById("species").value,
        breed: document.getElementById("breed").value,
        age: document.getElementById("age").value
            ? Number(document.getElementById("age").value)
            : null
    };

    try {
        const response = await fetch(API + "/animals", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(animal)
        });

        const result = await response.json();
        alert(result.message || result.error);

        if (response.ok) {
            event.target.reset();
            loadAnimals();
            loadDashboard();
        }
    } catch (error) {
        alert("Animal registration failed.");
    }
});

// Save health observation
document.getElementById("observationForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const id = document.getElementById("observationAnimalId").value;

    const observation = {
        temperature: Number(document.getElementById("temperature").value),
        notes: document.getElementById("notes").value
    };

    try {
        const response = await fetch(
            API + "/animals/" + id + "/observations",
            {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(observation)
            }
        );

        const result = await response.json();
        alert(result.message || result.error);

        if (response.ok) {
            event.target.reset();
            loadDashboard();
            loadAlerts();
        }
    } catch (error) {
        alert("Unable to save observation.");
    }
});

// Load alerts
async function loadAlerts() {
    try {
        const response = await fetch(API + "/alerts");
        const alerts = await response.json();

        let output = "";

        alerts.forEach(function(alertItem) {
            output += "<div class='item'>";
            output += "Animal ID: " + alertItem.animal_id;
            output += " | " + alertItem.message;
            output += " | Status: " + alertItem.status;

            if (alertItem.status === "New") {
                output += " <button onclick='acknowledgeAlert(" + alertItem.id + ")'>";
                output += "Acknowledge</button>";
            }

            output += "</div>";
        });

        if (output === "") {
            output = "No alerts available.";
        }

        document.getElementById("alertList").innerHTML = output;

    } catch (error) {
        alert("Unable to load alerts.");
    }
}

// Acknowledge alert
async function acknowledgeAlert(id) {
    try {
        const response = await fetch(
            API + "/alerts/" + id + "/acknowledge",
            {method: "POST"}
        );

        const result = await response.json();
        alert(result.message || result.error);

        loadAlerts();
        loadDashboard();

    } catch (error) {
        alert("Unable to acknowledge alert.");
    }
}

// Save vaccination
document.getElementById("vaccinationForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const id = document.getElementById("vaccineAnimalId").value;

    const vaccination = {
        vaccine_name: document.getElementById("vaccineName").value,
        vaccination_date: document.getElementById("vaccineDate").value
    };

    try {
        const response = await fetch(
            API + "/animals/" + id + "/vaccinations",
            {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(vaccination)
            }
        );

        const result = await response.json();
        alert(result.message || result.error);

        if (response.ok) {
            event.target.reset();
            loadDashboard();
        }

    } catch (error) {
        alert("Unable to save vaccination.");
    }
});

// Initial dashboard loading
loadDashboard();
loadAnimals();