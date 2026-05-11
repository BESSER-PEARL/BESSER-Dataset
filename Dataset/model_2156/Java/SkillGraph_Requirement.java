





import java.util.List;
import java.util.ArrayList;

public class SkillGraph_Requirement  {

    private String type;
    private String comment;
    private String term;



    public SkillGraph_Requirement(
        String type,        String comment,        String term    ) {
        this.type = type;
        this.comment = comment;
        this.term = term;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getTerm() {
        return term;
    }

    public void setTerm(String term) {
        this.term = term;
    }


}