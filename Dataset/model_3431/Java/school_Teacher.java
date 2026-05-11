





import java.util.List;
import java.util.ArrayList;

public class school_Teacher extends Person {






    private school_Student school_student;


    public school_Teacher(
    ) {
        super(
        );
    }



    public school_Student getSchool_student() {
        return school_student;
    }

    public void setSchool_student(school_Student school_student) {
        this.school_student = school_student;
    }

}