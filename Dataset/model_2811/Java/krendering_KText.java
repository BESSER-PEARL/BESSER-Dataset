





import java.util.List;
import java.util.ArrayList;

public class krendering_KText extends KRendering {

    private boolean cursorSelectable;
    private String text;
    private boolean editable;



    public krendering_KText(
        boolean cursorSelectable,        String text,        boolean editable    ) {
        super(
        );
        this.cursorSelectable = cursorSelectable;
        this.text = text;
        this.editable = editable;
    }


    public boolean getCursorselectable() {
        return cursorSelectable;
    }

    public void setCursorselectable(boolean cursorSelectable) {
        this.cursorSelectable = cursorSelectable;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public boolean getEditable() {
        return editable;
    }

    public void setEditable(boolean editable) {
        this.editable = editable;
    }


}