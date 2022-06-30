const app = {
  getCoordinates: async () => {
    try {
      const result = await fetch("http://localhost/iss/now");

      const { lat, lng } = await result.json();

      return { lat, lng };
    } catch (error) {
      console.log(error);
    }
  },

  initMap: async () => {
    const { lat, lng } = await app.getCoordinates();

    if (!document.querySelector(".leaflet-container")) {
      app.map = L.map("map").setView([lat, lng], 4);

      const altitude = document.querySelector(".alt");
      altitude.textContent = "430 km";
      const speed = document.querySelector("span.speed");
      speed.textContent = "27559 km/h";
      app.latitude = document.querySelector(".lat");
      app.longitude = document.querySelector(".lng");
      app.time = document.querySelector("span.time");
      app.date = document.querySelector("span.date");
    }

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 10,
      minZoom: 3,
      attribution: "© OpenStreetMap",
    }).addTo(app.map);

    const issIcon = L.icon({
      iconUrl: "img/iss.png",
      iconSize: [60, 60],
    });

    const marker = L.marker([lat, lng], { icon: issIcon });

    app.map.addLayer(marker);

    const date = new Date();
    app.latitude.textContent = Number(lat).toFixed(1);
    app.longitude.textContent = Number(lng).toFixed(1);
    app.time.textContent = dayjs(date).format("HH:mm:ss");
    app.date.textContent = dayjs(date).format("DD/MM/YYYY");

    setTimeout(() => {
      app.map.removeLayer(marker);
    }, 7999);
  },

  init: async () => {
    app.initMap();

    setInterval(() => {
      app.initMap();
    }, 8000);
  },
};

document.addEventListener("DOMContentLoaded", app.init);
