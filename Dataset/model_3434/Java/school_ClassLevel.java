





import java.util.List;
import java.util.ArrayList;

public class school_ClassLevel  {

    private int level;





    private school_ClassGroup school_classgroup;


    public school_ClassLevel(
        int level    ) {
        this.level = level;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public school_ClassGroup getSchool_classgroup() {
        return school_classgroup;
    }

    public void setSchool_classgroup(school_ClassGroup school_classgroup) {
        this.school_classgroup = school_classgroup;
    }

}