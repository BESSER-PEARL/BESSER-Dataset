





import java.util.List;
import java.util.ArrayList;

public class school_Student  {

    private String name;





    private school_ClassGroup school_classgroup;


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

    public school_ClassGroup getSchool_classgroup() {
        return school_classgroup;
    }

    public void setSchool_classgroup(school_ClassGroup school_classgroup) {
        this.school_classgroup = school_classgroup;
    }

}