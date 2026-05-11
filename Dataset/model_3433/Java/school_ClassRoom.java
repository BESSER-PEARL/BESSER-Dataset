





import java.util.List;
import java.util.ArrayList;

public class school_ClassRoom  {

    private int number;





    private List<school_Student> school_students;




    private school_School school_school;




    private school_Teacher school_teacher;


    public school_ClassRoom(
        int number    ) {
        this.number = number;
        this.school_students = new ArrayList<>();
    }

    public school_ClassRoom(
        int number        ArrayList<school_Student> school_students    ) {
        this.number = number;
        this.school_students = school_students;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public List<school_Student> getSchool_students() {
        return school_students;
    }

    public void addSchool_student(School_student school_student) {
        this.school_students.add(school_student);
    }
    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }
    public school_Teacher getSchool_teacher() {
        return school_teacher;
    }

    public void setSchool_teacher(school_Teacher school_teacher) {
        this.school_teacher = school_teacher;
    }

}