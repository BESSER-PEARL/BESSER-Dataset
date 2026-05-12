





import java.util.List;
import java.util.ArrayList;

public class Excel_ColOrRowElement extends TableElement {

    private String span;
    private String hidden;



    public Excel_ColOrRowElement(
        String span,        String hidden    ) {
        super(
        );
        this.span = span;
        this.hidden = hidden;
    }


    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
    }
    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }


}