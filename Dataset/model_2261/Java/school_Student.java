





import java.util.List;
import java.util.ArrayList;

public class school_Student  {

    private String name;





    private school_SchoolClass school_schoolclass;




    private school_SchoolClass school_schoolclass;




    private List<school_Student> school_students;


    public school_Student(
        String name    ) {
        this.name = name;
        this.school_students = new ArrayList<>();
    }

    public school_Student(
        String name        ArrayList<school_Student> school_students    ) {
        this.name = name;
        this.school_students = school_students;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public school_SchoolClass getSchool_schoolclass() {
        return school_schoolclass;
    }

    public void setSchool_schoolclass(school_SchoolClass school_schoolclass) {
        this.school_schoolclass = school_schoolclass;
    }
    public school_SchoolClass getSchool_schoolclass() {
        return school_schoolclass;
    }

    public void setSchool_schoolclass(school_SchoolClass school_schoolclass) {
        this.school_schoolclass = school_schoolclass;
    }
    public List<school_Student> getSchool_students() {
        return school_students;
    }

    public void addSchool_student(School_student school_student) {
        this.school_students.add(school_student);
    }

}