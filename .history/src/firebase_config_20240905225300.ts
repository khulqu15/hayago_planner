import { initializeApp } from 'firebase/app';
import { getStorage } from 'firebase/storage';
import { getFirestore } from 'firebase/firestore';
import { getDatabase, ref as dbRef, set, update, remove } from 'firebase/database';

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

const firebaseApp = initializeApp(firebaseConfig);

const firestore = getFirestore(firebaseApp);
const storage = getStorage(firebaseApp);
const database = getDatabase(firebaseApp)

export { firebaseApp, firestore, storage, database, dbRef, set, update, remove };
