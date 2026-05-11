





import java.util.List;
import java.util.ArrayList;

public class school_Student  {

    private String name;





    private school_Student school_student;




    private school_Classroom school_classroom;


    public school_Student(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public school_Student getSchool_student() {
        return school_student;
    }

    public void setSchool_student(school_Student school_student) {
        this.school_student = school_student;
    }
    public school_Classroom getSchool_classroom() {
        return school_classroom;
    }

    public void setSchool_classroom(school_Classroom school_classroom) {
        this.school_classroom = school_classroom;
    }

}