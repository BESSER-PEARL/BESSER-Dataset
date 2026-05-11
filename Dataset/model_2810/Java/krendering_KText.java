





import java.util.List;
import java.util.ArrayList;

public class krendering_KText extends KRendering {

    private boolean cursorSelectable;
    private boolean editable;
    private String text;



    public krendering_KText(
        boolean cursorSelectable,        boolean editable,        String text    ) {
        super(
        );
        this.cursorSelectable = cursorSelectable;
        this.editable = editable;
        this.text = text;
    }


    public boolean getCursorselectable() {
        return cursorSelectable;
    }

    public void setCursorselectable(boolean cursorSelectable) {
        this.cursorSelectable = cursorSelectable;
    }
    public boolean getEditable() {
        return editable;
    }

    public void setEditable(boolean editable) {
        this.editable = editable;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}