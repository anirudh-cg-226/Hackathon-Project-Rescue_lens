const mongoose=require('mongoose');

// Local MongoDB connection (for testing when Atlas is unavailable)
const mongoURI="mongodb://localhost:27017/Face_Recognition"

// Original MongoDB Atlas connection (uncomment when Atlas is fixed)
// const mongoURI="mongodb+srv://Garvit_Batra:!Ramprakash123@cluster0.eklye.mongodb.net/Face_Recognition?retryWrites=true&w=majority"

const connectToMongo = async () => {
    try {
        await mongoose.connect(mongoURI, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
            serverSelectionTimeoutMS: 5000,
            socketTimeoutMS: 45000,
        });
        console.log("✅ Connected to MongoDB successfully");
        console.log("📍 Using LOCAL MongoDB at localhost:27017");
    } catch (error) {
        console.error("❌ MongoDB connection error:", error.message);
        console.log("⚠️  Server will continue but database operations may fail");
        console.log("   Check if MongoDB is running: mongod --version");
    }
};

module.exports=connectToMongo;
