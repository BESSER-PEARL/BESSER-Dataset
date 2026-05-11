





import java.util.List;
import java.util.ArrayList;

public class ric_TextField extends FormControl {

    private int maxChars;
    private boolean readonly;
    private int charWidth;
    private boolean password;



    public ric_TextField(
        int maxChars,        boolean readonly,        int charWidth,        boolean password    ) {
        super(
        );
        this.maxChars = maxChars;
        this.readonly = readonly;
        this.charWidth = charWidth;
        this.password = password;
    }


    public int getMaxchars() {
        return maxChars;
    }

    public void setMaxchars(int maxChars) {
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
    public boolean getPassword() {
        return password;
    }

    public void setPassword(boolean password) {
        this.password = password;
    }


}