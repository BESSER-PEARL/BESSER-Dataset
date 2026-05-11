





import java.util.List;
import java.util.ArrayList;

public class swt_Combo extends AbstractList {

    private int textLimit;
    private String text;



    public swt_Combo(
        int textLimit,        String text    ) {
        super(
        );
        this.textLimit = textLimit;
        this.text = text;
    }


    public int getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(int textLimit) {
        this.textLimit = textLimit;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}