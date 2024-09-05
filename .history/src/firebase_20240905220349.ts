// firebase.ts
import { initializeApp } from 'firebase/app';
import { getStorage } from 'firebase/storage';
import { getFirestore } from 'firebase/firestore';
import { VueFire, VueFireFirestoreOptionsAPI } from 'vuefire';

// Your Firebase configuration (get these from your Firebase Console)
const firebaseConfig = {
    apiKey: "AIzaSyBi8dJvahsGnlEJxt2XW9CbCVCZ_F8QbIA",
    authDomain: "eco-enzym.firebaseapp.com",
    databaseURL: "https://eco-enzym-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "eco-enzym",
    storageBucket: "eco-enzym.appspot.com",
    messagingSenderId: "1090135367285",
    appId: "1:1090135367285:web:024ab437397e3ea199623c",
    measurementId: "G-57LTEMH91G"
  };

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);

// Initialize Firestore and Storage
const firestore = getFirestore(firebaseApp);
const storage = getStorage(firebaseApp);

export { firebaseApp, firestore, storage };
