





import java.util.List;
import java.util.ArrayList;

public class school_Room  {

    private String location;





    private school_ClassGroup school_classgroup;




    private school_Teacher school_teacher;


    public school_Room(
        String location    ) {
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public school_ClassGroup getSchool_classgroup() {
        return school_classgroup;
    }

    public void setSchool_classgroup(school_ClassGroup school_classgroup) {
        this.school_classgroup = school_classgroup;
    }
    public school_Teacher getSchool_teacher() {
        return school_teacher;
    }

    public void setSchool_teacher(school_Teacher school_teacher) {
        this.school_teacher = school_teacher;
    }

}