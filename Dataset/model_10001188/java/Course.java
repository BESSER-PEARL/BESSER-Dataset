





import java.util.List;
import java.util.ArrayList;

public class Course  {






    private List<Student1> student1s;




    private List<School_Admin> school_admins;


    public Course(
    ) {
        this.student1s = new ArrayList<>();
        this.school_admins = new ArrayList<>();
    }

    public Course(
        ArrayList<Student1> student1s,        ArrayList<School_Admin> school_admins    ) {
        this.student1s = student1s;
        this.school_admins = school_admins;
    }


    public List<Student1> getStudent1s() {
        return student1s;
    }

    public void addStudent1(Student1 student1) {
        this.student1s.add(student1);
    }
    public List<School_Admin> getSchool_admins() {
        return school_admins;
    }

    public void addSchool_admin(School_admin school_admin) {
        this.school_admins.add(school_admin);
    }

}