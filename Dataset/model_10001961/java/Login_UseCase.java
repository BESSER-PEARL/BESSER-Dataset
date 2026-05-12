





import java.util.List;
import java.util.ArrayList;

public class Login_UseCase  {






    private Traning_Admin_Actor traning_admin_actor;




    private Student_Actor student_actor;


    public Login_UseCase(
    ) {
    }



    public Traning_Admin_Actor getTraning_admin_actor() {
        return traning_admin_actor;
    }

    public void setTraning_admin_actor(Traning_Admin_Actor traning_admin_actor) {
        this.traning_admin_actor = traning_admin_actor;
    }
    public Student_Actor getStudent_actor() {
        return student_actor;
    }

    public void setStudent_actor(Student_Actor student_actor) {
        this.student_actor = student_actor;
    }

}