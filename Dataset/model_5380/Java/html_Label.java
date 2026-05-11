





import java.util.List;
import java.util.ArrayList;

public class html_Label extends FormElement {

    private String content;
    private int forText;



    public html_Label(
        String content,        int forText    ) {
        super(
        );
        this.content = content;
        this.forText = forText;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public int getFortext() {
        return forText;
    }

    public void setFortext(int forText) {
        this.forText = forText;
    }


}