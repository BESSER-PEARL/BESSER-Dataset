





import java.util.List;
import java.util.ArrayList;

public class bibTeX_ThesisEntry extends DatedEntry, TitledEntry, AuthoredEntry {

    private String school;



    public bibTeX_ThesisEntry(
        String school    ) {
        super(
        );
        this.school = school;
    }


    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }


}