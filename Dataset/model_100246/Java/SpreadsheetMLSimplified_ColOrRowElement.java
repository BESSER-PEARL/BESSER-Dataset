





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_ColOrRowElement extends TableElement {

    private boolean hidden;
    private int span;



    public SpreadsheetMLSimplified_ColOrRowElement(
        boolean hidden,        int span    ) {
        super(
        );
        this.hidden = hidden;
        this.span = span;
    }


    public boolean getHidden() {
        return hidden;
    }

    public void setHidden(boolean hidden) {
        this.hidden = hidden;
    }
    public int getSpan() {
        return span;
    }

    public void setSpan(int span) {
        this.span = span;
    }


}