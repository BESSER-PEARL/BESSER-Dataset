





import java.util.List;
import java.util.ArrayList;

public class school_Notation  {

    private int value;





    private school_Student school_student;


    public school_Notation(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public school_Student getSchool_student() {
        return school_student;
    }

    public void setSchool_student(school_Student school_student) {
        this.school_student = school_student;
    }

}