





import java.util.List;
import java.util.ArrayList;

public class cjsidl_messageSet  {

    private String inputComment;
    private String comment;
    private String outputComment;



    public cjsidl_messageSet(
        String inputComment,        String comment,        String outputComment    ) {
        this.inputComment = inputComment;
        this.comment = comment;
        this.outputComment = outputComment;
    }


    public String getInputcomment() {
        return inputComment;
    }

    public void setInputcomment(String inputComment) {
        this.inputComment = inputComment;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getOutputcomment() {
        return outputComment;
    }

    public void setOutputcomment(String outputComment) {
        this.outputComment = outputComment;
    }


}