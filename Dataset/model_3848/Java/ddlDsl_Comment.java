





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_Comment extends DdlStatement {

    private String comment;



    public ddlDsl_Comment(
        String comment    ) {
        super(
        );
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}