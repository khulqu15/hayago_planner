<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div id="container" class="w-full min-h-screen bg-base-300">
        <div class="w-full fixed top-0 left-0 p-4 flex justify-between items-center">
          <div class="flex items-center gap-3">
            <div>
              <button class="btn bg-base-300 hover:bg-base-200">Flight</button>
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