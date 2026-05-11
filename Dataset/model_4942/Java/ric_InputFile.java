





import java.util.List;
import java.util.ArrayList;

public class ric_InputFile extends FormControl {

    private boolean readonly;
    private int charWidth;
    private int maxChars;



    public ric_InputFile(
        boolean readonly,        int charWidth,        int maxChars    ) {
        super(
        );
        this.readonly = readonly;
        this.charWidth = charWidth;
        this.maxChars = maxChars;
    }


    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }
    public int getCharwidth() {
        return charWidth;
    }

    public void setCharwidth(int charWidth) {
        this.charWidth = charWidth;
    }
    public int getMaxchars() {
        return maxChars;
    }

    public void setMaxchars(int maxChars) {
        this.maxChars = maxChars;
    }


}