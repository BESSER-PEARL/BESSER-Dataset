





import java.util.List;
import java.util.ArrayList;

public class ClientRewiev  {

    private String text;
    private int mark;



    public ClientRewiev(
        String text,        int mark    ) {
        this.text = text;
        this.mark = mark;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getMark() {
        return mark;
    }

    public void setMark(int mark) {
        this.mark = mark;
    }


}