





import java.util.List;
import java.util.ArrayList;

public class model_Comment  {

    private String comment;





    private model_CommentableElement model_commentableelement;


    public model_Comment(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public model_CommentableElement getModel_commentableelement() {
        return model_commentableelement;
    }

    public void setModel_commentableelement(model_CommentableElement model_commentableelement) {
        this.model_commentableelement = model_commentableelement;
    }

}