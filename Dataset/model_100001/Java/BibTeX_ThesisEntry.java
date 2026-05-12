





import java.util.List;
import java.util.ArrayList;

public class BibTeX_ThesisEntry extends TitledEntry, DatedEntry, AuthoredEntry {

    private String school;



    public BibTeX_ThesisEntry(
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