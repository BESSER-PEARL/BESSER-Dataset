





import java.util.List;
import java.util.ArrayList;

public class ric_TextField extends FormControl {

    private boolean password;
    private int maxChars;
    private int charWidth;
    private boolean readonly;



    public ric_TextField(
        boolean password,        int maxChars,        int charWidth,        boolean readonly    ) {
        super(
        );
        this.password = password;
        this.maxChars = maxChars;
        this.charWidth = charWidth;
        this.readonly = readonly;
    }


    public boolean getPassword() {
        return password;
    }

    public void setPassword(boolean password) {
        this.password = password;
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