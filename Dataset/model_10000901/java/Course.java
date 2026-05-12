





import java.util.List;
import java.util.ArrayList;

public class Course  {






    private List<Student> students;




    private List<School_Admin> school_admins;


    public Course(
    ) {
        this.students = new ArrayList<>();
        this.school_admins = new ArrayList<>();
    }

    public Course(
        ArrayList<Student> students,        ArrayList<School_Admin> school_admins    ) {
        this.students = students;
        this.school_admins = school_admins;
    }


    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<School_Admin> getSchool_admins() {
        return school_admins;
    }

    public void addSchool_admin(School_admin school_admin) {
        this.school_admins.add(school_admin);
    }

}