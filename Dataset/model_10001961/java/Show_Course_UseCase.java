





import java.util.List;
import java.util.ArrayList;

public class Show_Course_UseCase  {






    private TEACHER_Actor teacher_actor;




    private Student_Actor student_actor;




    private CORPORATE_CLIENT_Actor corporate_client_actor;




    private Traning_Admin_Actor traning_admin_actor;


    public Show_Course_UseCase(
    ) {
    }



    public TEACHER_Actor getTeacher_actor() {
        return teacher_actor;
    }

    public void setTeacher_actor(TEACHER_Actor teacher_actor) {
        this.teacher_actor = teacher_actor;
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
    public Traning_Admin_Actor getTraning_admin_actor() {
        return traning_admin_actor;
    }

    public void setTraning_admin_actor(Traning_Admin_Actor traning_admin_actor) {
        this.traning_admin_actor = traning_admin_actor;
    }

}