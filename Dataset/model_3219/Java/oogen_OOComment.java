





import java.util.List;
import java.util.ArrayList;

public class oogen_OOComment  {

    private boolean isBlockComment;
    private String text;



    public oogen_OOComment(
        boolean isBlockComment,        String text    ) {
        this.isBlockComment = isBlockComment;
        this.text = text;
    }


    public boolean getIsblockcomment() {
        return isBlockComment;
    }

    public void setIsblockcomment(boolean isBlockComment) {
        this.isBlockComment = isBlockComment;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}