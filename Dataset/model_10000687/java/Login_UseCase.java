





import java.util.List;
import java.util.ArrayList;

public class Login_UseCase  {






    private Faculty__Actor faculty__actor;




    private Student_Actor student_actor;


    public Login_UseCase(
    ) {
    }



    public Faculty__Actor getFaculty__actor() {
        return faculty__actor;
    }

    public void setFaculty__actor(Faculty__Actor faculty__actor) {
        this.faculty__actor = faculty__actor;
    }
    public Student_Actor getStudent_actor() {
        return student_actor;
    }

    public void setStudent_actor(Student_Actor student_actor) {
        this.student_actor = student_actor;
    }

}