





import java.util.List;
import java.util.ArrayList;

public class dbmodel_ClassOrDuplicate  {

    private String name;
    private String reps;
    private String abbrev;



    public dbmodel_ClassOrDuplicate(
        String name,        String reps,        String abbrev    ) {
        this.name = name;
        this.reps = reps;
        this.abbrev = abbrev;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReps() {
        return reps;
    }

    public void setReps(String reps) {
        this.reps = reps;
    }
    public String getAbbrev() {
        return abbrev;
    }

    public void setAbbrev(String abbrev) {
        this.abbrev = abbrev;
    }


}