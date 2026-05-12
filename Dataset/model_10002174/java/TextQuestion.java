





import java.util.List;
import java.util.ArrayList;

public class TextQuestion  {

    private String text;
    private boolean caseSensitive;



    public TextQuestion(
        String text,        boolean caseSensitive    ) {
        this.text = text;
        this.caseSensitive = caseSensitive;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public boolean getCasesensitive() {
        return caseSensitive;
    }

    public void setCasesensitive(boolean caseSensitive) {
        this.caseSensitive = caseSensitive;
    }


}