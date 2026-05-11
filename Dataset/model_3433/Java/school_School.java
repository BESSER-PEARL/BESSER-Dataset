





import java.util.List;
import java.util.ArrayList;

public class school_School  {

    private int rank;
    private String name;





    private List<school_Student> school_students;




    private List<school_Teacher> school_teachers;




    private school_Academy school_academy;


    public school_School(
        int rank,        String name    ) {
        this.rank = rank;
        this.name = name;
        this.school_students = new ArrayList<>();
        this.school_teachers = new ArrayList<>();
    }

    public school_School(
        int rank,        String name        ArrayList<school_Student> school_students,        ArrayList<school_Teacher> school_teachers    ) {
        this.rank = rank;
        this.name = name;
        this.school_students = school_students;
        this.school_teachers = school_teachers;
    }

    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<school_Student> getSchool_students() {
        return school_students;
    }

    public void addSchool_student(School_student school_student) {
        this.school_students.add(school_student);
    }
    public List<school_Teacher> getSchool_teachers() {
        return school_teachers;
    }

    public void addSchool_teacher(School_teacher school_teacher) {
        this.school_teachers.add(school_teacher);
    }
    public school_Academy getSchool_academy() {
        return school_academy;
    }

    public void setSchool_academy(school_Academy school_academy) {
        this.school_academy = school_academy;
    }

}