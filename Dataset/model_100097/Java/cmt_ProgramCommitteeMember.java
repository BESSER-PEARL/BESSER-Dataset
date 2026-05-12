





import java.util.List;
import java.util.ArrayList;

public class cmt_ProgramCommitteeMember extends ConferenceMember, Person {

    private String maxPapers;



    public cmt_ProgramCommitteeMember(
        String maxPapers    ) {
        super(
        );
        this.maxPapers = maxPapers;
    }


    public String getMaxpapers() {
        return maxPapers;
    }

    public void setMaxpapers(String maxPapers) {
        this.maxPapers = maxPapers;
    }


}