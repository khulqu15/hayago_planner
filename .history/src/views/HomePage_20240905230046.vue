<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div id="container" class="w-full min-h-screen bg-base-300 text-base-content">
        <div class="w-full fixed top-0 z-[100] left-0 p-3 flex bg-base-300 justify-between items-center">
          <div class="lg:hidden flex">
            <div>
              <button @click="show_drawer = !show_drawer" class="btn bg-base-300 hover:bg-base-200"><Icon icon="mingcute:menu-line"/></button>
            </div>
          </div>
          <div v-if="show_drawer" class="fixed top-0 left-0 p-8 min-h-screen bg-base-300 shadow-2xl space-y-2 z-10 max-w-sm w-full items-center gap-2">
            <div>
              <button @click="show_drawer = !show_drawer" class="btn bg-base-200 hover:bg-base-100"><Icon class="text-2xl" icon="material-symbols:close"/> Close</button>
            </div>
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Data</button>
            </div>
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Plan</button>
            </div>
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Setup</button>
            </div>
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Simulation</button>
            </div>
          </div>
          <div class="lg:flex hidden items-center gap-2">
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Data</button>
            </div>
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Plan</button>
            </div>
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Setup</button>
            </div>
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Simulation</button>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <div>
              <select v-model="baudrate" class="select select-bordered w-full max-w-xs">
                <option :value="null" disabled selected>Baudrate</option>
                <option value="115200">115200</option>
                <option value="9600">9600</option>
              </select>
            </div>
            <div>
              <select v-model="copter" class="select select-bordered w-full max-w-xs">
                <option :value="null" disabled selected>Copter</option>
                <option value="115200">Copter 1</option>
              </select>
            </div>
            <div>
              <button class="btn bg-blue-700 hover:bg-base-600 text-white">Connect</button>
            </div>
          </div>
        </div>

        <div class="pt-24 pb-8 px-8 w-full">
          <div class="w-full grid grid-cols-3 gap-3">
            <div class="md:col-span-1 col-span-3 space-y-3">
              <div class="w-full bg-blue-600 h-[50vh] min-h-[50vh] overflow-hidden rounded-2xl">
                <l-map class="w-full h-[50vh] rounded-2xl" ref="map" :use-global-leaflet="false" v-model="zoom" v-model:zoom="zoom" :center="[-7.276606, 112.793865]" @click="addWaypoint">
                  <l-tile-layer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    layer-type="base"
                    name="OpenStreetMap">
                  </l-tile-layer>
                  <l-marker v-for="(waypoint, index) in waypoints" :key="index" :lat-lng="[waypoint.lat, waypoint.lng]"></l-marker>
                  <l-polyline :lat-lngs="waypointCoords" color="blue"></l-polyline>
                </l-map>
              </div>
              <div class="w-full bg-base-200 space-y-3 min-h-[25vh] h-[25vh] overflow-y-auto p-4 rounded-2xl">
                <div v-for="(waypoint, index) in waypoints" :key="index" class="flex items-center justify-between">
                  <div class="font-bold">{{ waypoint.name }}</div>
                  <div class="text-sm">{{ waypoint.lat }}, {{ waypoint.lng }}</div>
                  <div class="flex items-center gap-3">
                    <button class="btn btn-error btn-sm" @click="deleteWaypoint(index)">
                      <Icon icon="streamline:delete-1" />
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="md:col-span-2 col-span-3 space-y-3">
              <div class="w-full bg-blue-600 relative min-h-[50vh] h-[50vh] overflow-hidden rounded-2xl">
                <div class="absolute text-sm right-0 top-0 p-3 m-3 rounded-xl bg-blue-500 text-white flex items-center gap-2">
                  <Icon icon="solar:camera-bold"/> 
                  <span>Live Camera</span>
                </div>
                <img v-if="url" :src="url" :alt="url" class="w-full h-full object-center object-cover">
              </div>
              <div class="w-full bg-base-200 min-h-[25vh] p-2 rounded-2xl">
                <div class="w-full grid grid-cols-3">
                  <div class="lg:col-span-1 col-span-3 w-full h-[23vh] rounded-xl flex items-center justify-center">
                    <div class="text-center">
                      <h1 class="text-xs">Latitude</h1>
                      <div class="font-bold">-7.276606</div>
                      <h1 class="text-sm mt-4">Longitude</h1>
                      <div class="font-bold">112.793865</div>
                    </div>
                  </div>
                  <div class="lg:col-span-2 col-span-3 w-full min-h-[23vh] lg:py-0 py-6 bg-base-100 rounded-xl grid md:grid-cols-3 grid-cols-2 items-center justify-center">
                      <div class="text-center">
                        <h1 class="text-sm">Altitude</h1>
                        <div class="font-bold">18.5 m</div>
                        <h1 class="text-sm mt-4">Speed</h1>
                        <div class="font-bold">22 km/h</div>
                      </div>
                      <div class="text-center">
                        <h1 class="text-sm">Travel</h1>
                        <div class="font-bold">2.1 km</div>
                        <h1 class="text-sm mt-4">Duration</h1>
                        <div class="font-bold">34:04</div>
                      </div>
                      <div class="text-center">
                        <h1 class="text-sm">Tank</h1>
                        <div class="font-bold">1.53 l</div>
                        <h1 class="text-sm mt-4">Battery</h1>
                        <div class="font-bold">80 %</div>
                      </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue'
import { Icon } from '@iconify/vue'
import "leaflet/dist/leaflet.css"
import { database, dbRef, set, update, remove } from "@/firebase_config"
import { LMap, LTileLayer, LMarker, LPolyline } from "@vue-leaflet/vue-leaflet"
import { computed, onMounted, ref, Ref } from 'vue';
import { ref as storageRef } from 'firebase/storage'
import { useFirebaseStorage, useStorageFile } from 'vuefire'
import { onValue } from 'firebase/database'

const storage = useFirebaseStorage()
const mountainFileRef = storageRef(storage, 'data/1.jpg')

const { url, uploadProgress, uploadError, uploadTask, upload } = useStorageFile(mountainFileRef)

const baudrate: Ref<any> = ref(null)
const copter: Ref<any> = ref(null)
const show_drawer: Ref<boolean> = ref(false)
const zoom: Ref<number> = ref(18)

const waypoints = ref([
  { name: 'Home', lat: -7.276606, lng: 112.793865 }
]);
const waypointsRef = dbRef(database, 'waypoints');
const waypointCoords = computed(() => {
  return waypoints.value.map(waypoint => [waypoint.lat, waypoint.lng]);
});

onMounted(() => {
  onValue(waypointsRef, (snapshot) => {
    const data = snapshot.val();

    if (data) {
      waypoints.value = Object.keys(data).map((key) => ({
        name: data[key].name,
        lat: data[key].lat,
        lng: data[key].lon, 
      }));
    }
  });
})

const addWaypoint = (e: any) => {
  const newWaypoint = {
    name: `Waypoint ${waypoints.value.length}`,
    lat: e.latlng.lat,
    lng: e.latlng.lng,
  };
  waypoints.value.push(newWaypoint);
  syncWaypointsToFirebase()
};

const syncWaypointsToFirebase = () => {
  const waypointsData = waypoints.value.reduce((acc: any, waypoint, index) => {
    acc[index] = {
      name: waypoint.name,
      lat: waypoint.lat,
      lon: waypoint.lng,
    };
    return acc;
  }, {});

  set(waypointsRef, waypointsData);
};

const deleteWaypoint = (index: number) => {
  waypoints.value.splice(index, 1);
  syncWaypointsToFirebase();
};
</script>