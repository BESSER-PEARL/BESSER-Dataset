





import java.util.List;
import java.util.ArrayList;

public class ric_InputFile extends FormControl {

    private int maxChars;
    private int charWidth;
    private boolean readonly;



    public ric_InputFile(
        int maxChars,        int charWidth,        boolean readonly    ) {
        super(
        );
        this.maxChars = maxChars;
        this.charWidth = charWidth;
        this.readonly = readonly;
    }


    public int getMaxchars() {
        return maxChars;
    }

    public void setMaxchars(int maxChars) {
        this.maxChars = maxChars;
    }
    public int getCharwidth() {
        return charWidth;
    }

    public void setCharwidth(int charWidth) {
        this.charWidth = charWidth;
    }
    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }


}