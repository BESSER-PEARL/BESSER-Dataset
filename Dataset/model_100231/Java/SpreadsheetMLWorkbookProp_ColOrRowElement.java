





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_ColOrRowElement extends TableElement {

    private String hidden;
    private String span;



    public SpreadsheetMLWorkbookProp_ColOrRowElement(
        String hidden,        String span    ) {
        super(
        );
        this.hidden = hidden;
        this.span = span;
    }


    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
    }


}