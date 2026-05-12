





import java.util.List;
import java.util.ArrayList;

public class Logout_UseCase  {






    private Admin_Actor admin_actor;




    private Student_Actor student_actor;




    private Faculty__Actor faculty__actor;


    public Logout_UseCase(
    ) {
    }



    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }
    public Student_Actor getStudent_actor() {
        return student_actor;
    }

    public void setStudent_actor(Student_Actor student_actor) {
        this.student_actor = student_actor;
    }
    public Faculty__Actor getFaculty__actor() {
        return faculty__actor;
    }

    public void setFaculty__actor(Faculty__Actor faculty__actor) {
        this.faculty__actor = faculty__actor;
    }

}