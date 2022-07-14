function updateDescription(name){
  const all = getJSONGroup(locations, "name", name);
  document.getElementById("loc_name").innerHTML = name;
  document.getElementById("loc_desc").innerHTML = all.description;

}

function getJSONGroup(array, key, value) {
  return array.filter((object) => {
      return object[key] === value;
  })[0];
};

function onClick() {
    const locName = this.getPopup().getContent();
    updateDescription(locName);  
}

function loadLocations() {
  for(let index=0; index < locations.length; index++){
      let popupText = locations[index].namel
      let coord = [locations[index].lat, locations[index].lon];
      let newLoc = new L.marker(coord).bindPopup(popupText).addTo(map).on('click', onClick);
  }
}

async function main() {
  const locs = await fetch("/adventures/locations").then(response => response.json());
  locations = locs.locations;
  loadLocations();
}

void main();
