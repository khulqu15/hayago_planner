<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div id="container" class="w-full min-h-screen bg-base-300">
        <div class="w-full fixed top-0 left-0 p-3 flex justify-between items-center">
          <div class="flex items-center gap-2">
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
              <select class="select select-bordered w-full max-w-xs">
                <option disabled selected>Baudrate</option>
                <option>Han Solo</option>
                <option>Greedo</option>
              </select>
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
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
</script>