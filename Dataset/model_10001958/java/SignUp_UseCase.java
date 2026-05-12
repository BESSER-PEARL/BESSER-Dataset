





import java.util.List;
import java.util.ArrayList;

public class SignUp_UseCase  {






    private Student_Actor student_actor;




    private Faculty__Actor faculty__actor;


    public SignUp_UseCase(
    ) {
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