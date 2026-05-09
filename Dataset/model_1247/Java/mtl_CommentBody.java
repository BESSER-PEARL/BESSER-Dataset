





import java.util.List;
import java.util.ArrayList;

public class mtl_CommentBody  {

    private int endPosition;
    private int startPosition;
    private String value;





    private mtl_Comment mtl_comment;


    public mtl_CommentBody(
        int endPosition,        int startPosition,        String value    ) {
        this.endPosition = endPosition;
        this.startPosition = startPosition;
        this.value = value;
    }


    public int getEndposition() {
        return endPosition;
    }

    public void setEndposition(int endPosition) {
        this.endPosition = endPosition;
    }
    public int getStartposition() {
        return startPosition;
    }

    public void setStartposition(int startPosition) {
        this.startPosition = startPosition;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public mtl_Comment getMtl_comment() {
        return mtl_comment;
    }

    public void setMtl_comment(mtl_Comment mtl_comment) {
        this.mtl_comment = mtl_comment;
    }

}