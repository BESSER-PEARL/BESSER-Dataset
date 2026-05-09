





import java.util.List;
import java.util.ArrayList;

public class jointPackage_BibTeX2DocBook_SrcThesisEntry extends SrcDatedEntry, SrcTitledEntry, SrcAuthoredEntry {

    private String school;



    public jointPackage_BibTeX2DocBook_SrcThesisEntry(
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