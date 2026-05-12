





import java.util.List;
import java.util.ArrayList;

public class Administrator  {






    private cmt_Reviewer cmt_reviewer;




    private cmt_ProgramCommitteeMember cmt_programcommitteemember;


    public Administrator(
    ) {
    }



    public cmt_Reviewer getCmt_reviewer() {
        return cmt_reviewer;
    }

    public void setCmt_reviewer(cmt_Reviewer cmt_reviewer) {
        this.cmt_reviewer = cmt_reviewer;
    }
    public cmt_ProgramCommitteeMember getCmt_programcommitteemember() {
        return cmt_programcommitteemember;
    }

    public void setCmt_programcommitteemember(cmt_ProgramCommitteeMember cmt_programcommitteemember) {
        this.cmt_programcommitteemember = cmt_programcommitteemember;
    }

}