





import java.util.List;
import java.util.ArrayList;

public class model_TMCLConstruct extends OnoObject {

    private String description;
    private String comment;
    private String see_also;



    public model_TMCLConstruct(
        String description,        String comment,        String see_also    ) {
        super(
        );
        this.description = description;
        this.comment = comment;
        this.see_also = see_also;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getSee_also() {
        return see_also;
    }

    public void setSee_also(String see_also) {
        this.see_also = see_also;
    }


}