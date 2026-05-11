





import java.util.List;
import java.util.ArrayList;

public class school_Query  {

    private String type;





    private school_Student school_student;


    public school_Query(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public school_Student getSchool_student() {
        return school_student;
    }

    public void setSchool_student(school_Student school_student) {
        this.school_student = school_student;
    }

}