





import java.util.List;
import java.util.ArrayList;

public class school_Pupil  {

    private String name;





    private school_School school_school;


    public school_Pupil(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }

}