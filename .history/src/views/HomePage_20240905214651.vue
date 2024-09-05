<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div id="container" class="w-full min-h-screen bg-base-300 text-base-content">
        <div class="w-full fixed top-0 left-0 p-3 flex bg-base-300 justify-between items-center">
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
            <div class="col-span-2">
              <div class="w-full bg-blue-600 h-[60vh] rounded-2xl"></div>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate ad autem unde obcaecati distinctio voluptates modi ipsum facere et molestiae. Totam fugiat pariatur mollitia quisquam quam quos similique, voluptatibus id, quo voluptatum, quis velit officiis ut perspiciatis nam provident itaque hic fuga voluptatem. Ea, hic, repudiandae porro cupiditate modi quisquam doloremque sunt, nobis iusto quas natus dicta sapiente inventore dolorum non ipsum. Quod sed laboriosam vero odit ipsa molestias magnam maiores delectus, numquam sequi, perferendis unde? Repudiandae dolorem tempora quam eius? Culpa, itaque suscipit sit laboriosam officiis ea provident similique tempore exercitationem cum, dicta asperiores tenetur veniam, hic cupiditate velit?
            </div>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
import { Icon } from '@iconify/vue'
import { ref, Ref } from 'vue';

const baudrate: Ref<any> = ref(null)
const copter: Ref<any> = ref(null)
const show_drawer: Ref<boolean> = ref(false)
</script>