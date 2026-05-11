





import java.util.List;
import java.util.ArrayList;

public class school_SchoolModel  {






    private List<school_School> school_schools;


    public school_SchoolModel(
    ) {
        this.school_schools = new ArrayList<>();
    }

    public school_SchoolModel(
        ArrayList<school_School> school_schools    ) {
        this.school_schools = school_schools;
    }


    public List<school_School> getSchool_schools() {
        return school_schools;
    }

    public void addSchool_school(School_school school_school) {
        this.school_schools.add(school_school);
    }

}