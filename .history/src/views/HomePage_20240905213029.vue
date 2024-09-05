<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div id="container" class="w-full min-h-screen bg-base-300">
        <div class="w-full fixed top-0 left-0 p-12"></div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
</script>