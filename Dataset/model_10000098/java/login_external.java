





import java.util.List;
import java.util.ArrayList;

public class login_external  {






    private Teacher_Actor teacher_actor;




    private parent_Actor parent_actor;




    private student_Actor student_actor;




    private admin_Actor admin_actor;


    public login_external(
    ) {
    }



    public Teacher_Actor getTeacher_actor() {
        return teacher_actor;
    }

    public void setTeacher_actor(Teacher_Actor teacher_actor) {
        this.teacher_actor = teacher_actor;
    }
    public parent_Actor getParent_actor() {
        return parent_actor;
    }

    public void setParent_actor(parent_Actor parent_actor) {
        this.parent_actor = parent_actor;
    }
    public student_Actor getStudent_actor() {
        return student_actor;
    }

    public void setStudent_actor(student_Actor student_actor) {
        this.student_actor = student_actor;
    }
    public admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }

}