function main() {  
  const origin = [39.833333, -98.583333]; // This is the center of the contiguous United States

  map = L.map('map', {
    maxZoom: 19,
    minZoom: 1,
    }).setView(origin, 4);
  
  // OSM Tiles
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 20,
      maxNativeZoom: 20,
  attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap Contributors</a>'
  }).addTo(map);
  
  // show the scale bar on the lower left corner
  L.control.scale({imperial: true, metric: true}).addTo(map);
};

void main();
