





import java.util.List;
import java.util.ArrayList;

public class Course  {






    private List<School_Admin> school_admins;




    private List<Student> students;


    public Course(
    ) {
        this.school_admins = new ArrayList<>();
        this.students = new ArrayList<>();
    }

    public Course(
        ArrayList<School_Admin> school_admins,        ArrayList<Student> students    ) {
        this.school_admins = school_admins;
        this.students = students;
    }


    public List<School_Admin> getSchool_admins() {
        return school_admins;
    }

    public void addSchool_admin(School_admin school_admin) {
        this.school_admins.add(school_admin);
    }
    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}