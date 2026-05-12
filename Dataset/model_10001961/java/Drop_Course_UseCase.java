





import java.util.List;
import java.util.ArrayList;

public class Drop_Course_UseCase  {






    private Student_Actor student_actor;




    private CORPORATE_CLIENT_Actor corporate_client_actor;


    public Drop_Course_UseCase(
    ) {
    }



    public Student_Actor getStudent_actor() {
        return student_actor;
    }

    public void setStudent_actor(Student_Actor student_actor) {
        this.student_actor = student_actor;
    }
    public CORPORATE_CLIENT_Actor getCorporate_client_actor() {
        return corporate_client_actor;
    }

    public void setCorporate_client_actor(CORPORATE_CLIENT_Actor corporate_client_actor) {
        this.corporate_client_actor = corporate_client_actor;
    }

}