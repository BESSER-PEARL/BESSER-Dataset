





import java.util.List;
import java.util.ArrayList;

public class jointPackage_SrcThesisEntry extends SrcDatedEntry, SrcTitledEntry, SrcAuthoredEntry {

    private String school;



    public jointPackage_SrcThesisEntry(
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