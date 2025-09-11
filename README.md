# Tuition Media Platform

An online platform connecting students/parents with tutors for finding and managing tuition services.

## 🌟 Features

### 1. User Registration and Authentication
- Dual role system (Users and Tutors)
- Separate registration and login flows
- Email verification system
- Secure authentication mechanism

### 2. Tuition Management (Tutor Exclusive)
- Tutors can add new tuition listings
- Edit existing tuition details
- Delete tuition offerings
- Comprehensive tuition information (title, description, class, subject, availability)

### 3. Profile Management
- Detailed profile pages for both Users and Tutors
- Applied tuition history for Users
- Posted tuition overview for Tutors
- Password change functionality

### 4. Advanced Filtering System
- Filter tuitions by class level
- Filter by subject category
- Search by tutor name/profile
- Combined filtering options

### 5. Tuition Application System
- One-click application process for Users
- Applicant management dashboard for Tutors
- Selection system for Tutors to choose applicants
- Application status tracking

### 6. Progress Tracking
**For Tutors:**
- Student progress monitoring
- Topic completion marking
- Assignment creation and management

**For Students:**
- Progress visualization
- Completed topics overview
- Assignment tracking

### 7. Review System
- Post-selection review capability
- Rating system for completed tuitions
- Review visibility controls

### 8. Deployment Ready
- Full deployment documentation
- Hosting configuration guidelines
- Environment setup instructions

### 9. Payment Gateway Ready (Future Implementation)
- Architecture designed for payment integration
- Tuition fee processing foundation
- Earnings management system framework
- Transaction history infrastructure

## 🛠️ Technology Stack

- **Frontend:** React.js with Tailwind CSS
- **Backend:** Django and DRF
- **Database:** PostGreSQL
- **Authentication:** JWT with email verification
- **Deployment:** Vercel/Netlify (Frontend), Heroku/Railway (Backend)

## 📋 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/tuition-media-platform.git
   cd tuition-media-platform
   ```

2. **Install dependencies**
   ```bash
   # Install backend dependencies
   cd backend
   npm install
   
   # Install frontend dependencies
   cd ../frontend
   npm install
   ```

3. **Environment Configuration**
   - Create `.env` files in both frontend and backend directories
   - Configure database connection, JWT secret, and email service credentials

4. **Database Setup**
   ```bash
   # Ensure MongoDB is running
   mongod
   ```

5. **Run the application**
   ```bash
   # Start backend server
   cd backend
   npm run dev
   
   # Start frontend (in separate terminal)
   cd frontend
   npm start
   ```

## 🚀 Deployment

The application is deployed on a secure hosting platform with the following components:

- **Frontend:** Hosted on [Platform Name]
- **Backend:** API deployed on [Vercel]
- **Database:** MongoDB hosted on [SupaBase]

Live Demo: [https://tutorix-blond.vercel.app/]

## 📁 Project Structure

```
tuition-media-platform/
├── backend/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   └── config/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── context/
│   │   └── utils/
└── documentation/
```

## 🔧 API Documentation

The API endpoints are documented using Swagger. Access the full API documentation at [https://tutorix-blond.vercel.app/docs/] after running the development server.

## 👥 User Roles

### Tutor
- Create and manage tuition listings
- View and select applicants
- Track student progress
- Manage assignments

### User (Student/Parent)
- Browse and search for tuitions
- Apply for tuitions
- Track application status
- View progress and assignments
- Leave reviews

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GPL License - see the [LICENSE.md](LICENSE.md) file for details.

## 📞 Support

For support, email support@tutorix.org or join our Slack channel.

## 🎯 Future Enhancements

- Payment gateway integration
- Video conferencing capabilities
- Advanced analytics dashboard
- Mobile application development
- Multi-language support

---

**Note:** This project was developed as part of an academic requirement focusing on creating a seamless connection between students and tutors in the educational domain.
