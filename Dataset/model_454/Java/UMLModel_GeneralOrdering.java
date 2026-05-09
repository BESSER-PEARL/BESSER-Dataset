





import java.util.List;
import java.util.ArrayList;

public class UMLModel_GeneralOrdering extends NamedElement {

    private String after;
    private String before;



    public UMLModel_GeneralOrdering(
        String after,        String before    ) {
        super(
        );
        this.after = after;
        this.before = before;
    }


    public String getAfter() {
        return after;
    }

    public void setAfter(String after) {
        this.after = after;
    }
    public String getBefore() {
        return before;
    }

    public void setBefore(String before) {
        this.before = before;
    }


}