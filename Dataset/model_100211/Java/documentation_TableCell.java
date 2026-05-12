





import java.util.List;
import java.util.ArrayList;

public class documentation_TableCell  {

    private String content;
    private int span;



    public documentation_TableCell(
        String content,        int span    ) {
        this.content = content;
        this.span = span;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public int getSpan() {
        return span;
    }

    public void setSpan(int span) {
        this.span = span;
    }


}