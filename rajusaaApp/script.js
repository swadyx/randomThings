const map = L.map("map").setView([60.4737, 25.0899], 10);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "&copy; OpenStreetMap contributors"
}).addTo(map);

let marker = null;


map.on("click", async function(event) {

    const latitude = event.latlng.lat;
    const longitude = event.latlng.lng;

    console.log("Klikkasit:", latitude, longitude);

    if (marker) {
        map.removeLayer(marker);
    }

    marker = L.marker([latitude, longitude]).addTo(map);

    document.getElementById("location").textContent =
        "Haetaan sijaintia...";

    document.getElementById("weather").innerHTML =
        "<p>Haetaan säätietoja...</p>";


    const locationResponse = await fetch(
        `https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json&accept-language=fi`
    );

    const locationData = await locationResponse.json();



    const address = locationData.address;

    const city =
        address.city ||
        address.town ||
        address.municipality ||
        address.village ||
        "Tuntematon sijainti";


    document.getElementById("location").textContent = city;


    const weatherResponse = await fetch(
        `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,wind_speed_10m,weather_code`
    );

    const weatherData = await weatherResponse.json();

    console.log(weatherData);


    const temperature =
        weatherData.current.temperature_2m;

    const wind =
        weatherData.current.wind_speed_10m;


    document.getElementById("weather").innerHTML = `
        <p>Lämpötila: ${temperature} °C</p>
        <p>Tuuli: ${wind} km/h</p>
    `;
});
