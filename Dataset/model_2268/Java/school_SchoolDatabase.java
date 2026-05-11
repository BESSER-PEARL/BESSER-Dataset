





import java.util.List;
import java.util.ArrayList;

public class school_SchoolDatabase  {






    private List<school_Query> school_querys;




    private school_School school_school;


    public school_SchoolDatabase(
    ) {
        this.school_querys = new ArrayList<>();
    }

    public school_SchoolDatabase(
        ArrayList<school_Query> school_querys    ) {
        this.school_querys = school_querys;
    }


    public List<school_Query> getSchool_querys() {
        return school_querys;
    }

    public void addSchool_query(School_query school_query) {
        this.school_querys.add(school_query);
    }
    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }

}