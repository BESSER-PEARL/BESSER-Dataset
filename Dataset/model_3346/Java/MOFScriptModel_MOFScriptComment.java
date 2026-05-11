





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_MOFScriptComment extends MOFScriptObject {

    private boolean singleLine;
    private boolean docStyle;
    private String commentText;



    public MOFScriptModel_MOFScriptComment(
        boolean singleLine,        boolean docStyle,        String commentText    ) {
        super(
        );
        this.singleLine = singleLine;
        this.docStyle = docStyle;
        this.commentText = commentText;
    }


    public boolean getSingleline() {
        return singleLine;
    }

    public void setSingleline(boolean singleLine) {
        this.singleLine = singleLine;
    }
    public boolean getDocstyle() {
        return docStyle;
    }

    public void setDocstyle(boolean docStyle) {
        this.docStyle = docStyle;
    }
    public String getCommenttext() {
        return commentText;
    }

    public void setCommenttext(String commentText) {
        this.commentText = commentText;
    }


}