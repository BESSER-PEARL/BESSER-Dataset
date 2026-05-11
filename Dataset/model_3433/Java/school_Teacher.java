





import java.util.List;
import java.util.ArrayList;

public class school_Teacher  {

    private String name;





    private school_Academy school_academy;


    public school_Teacher(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public school_Academy getSchool_academy() {
        return school_academy;
    }

    public void setSchool_academy(school_Academy school_academy) {
        this.school_academy = school_academy;
    }

}