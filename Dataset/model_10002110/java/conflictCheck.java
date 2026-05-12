





import java.util.List;
import java.util.ArrayList;

public class conflictCheck  {

    private String subjects;
    private boolean conflict;



    public conflictCheck(
        String subjects,        boolean conflict    ) {
        this.subjects = subjects;
        this.conflict = conflict;
    }


    public String getSubjects() {
        return subjects;
    }

    public void setSubjects(String subjects) {
        this.subjects = subjects;
    }
    public boolean getConflict() {
        return conflict;
    }

    public void setConflict(boolean conflict) {
        this.conflict = conflict;
    }


}