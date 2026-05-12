





import java.util.List;
import java.util.ArrayList;

public class Logout_UseCase  {






    private Admin_Actor admin_actor;




    private Instructor_Actor instructor_actor;




    private Student_Actor student_actor;


    public Logout_UseCase(
    ) {
    }



    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }
    public Instructor_Actor getInstructor_actor() {
        return instructor_actor;
    }

    public void setInstructor_actor(Instructor_Actor instructor_actor) {
        this.instructor_actor = instructor_actor;
    }
    public Student_Actor getStudent_actor() {
        return student_actor;
    }

    public void setStudent_actor(Student_Actor student_actor) {
        this.student_actor = student_actor;
    }

}