





import java.util.List;
import java.util.ArrayList;

public class logout_external  {






    private admin_Actor admin_actor;




    private student_Actor student_actor;




    private parent_Actor parent_actor;




    private faculty_Actor faculty_actor;


    public logout_external(
    ) {
    }



    public admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }
    public student_Actor getStudent_actor() {
        return student_actor;
    }

    public void setStudent_actor(student_Actor student_actor) {
        this.student_actor = student_actor;
    }
    public parent_Actor getParent_actor() {
        return parent_actor;
    }

    public void setParent_actor(parent_Actor parent_actor) {
        this.parent_actor = parent_actor;
    }
    public faculty_Actor getFaculty_actor() {
        return faculty_actor;
    }

    public void setFaculty_actor(faculty_Actor faculty_actor) {
        this.faculty_actor = faculty_actor;
    }

}