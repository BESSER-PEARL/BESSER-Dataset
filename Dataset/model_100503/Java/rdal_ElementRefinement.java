





import java.util.List;
import java.util.ArrayList;

public class rdal_ElementRefinement extends IdentifiedElement {

    private String refinedElementEntries;
    private String subElementRefEntries;



    public rdal_ElementRefinement(
        String refinedElementEntries,        String subElementRefEntries    ) {
        super(
        );
        this.refinedElementEntries = refinedElementEntries;
        this.subElementRefEntries = subElementRefEntries;
    }


    public String getRefinedelemententries() {
        return refinedElementEntries;
    }

    public void setRefinedelemententries(String refinedElementEntries) {
        this.refinedElementEntries = refinedElementEntries;
    }
    public String getSubelementrefentries() {
        return subElementRefEntries;
    }

    public void setSubelementrefentries(String subElementRefEntries) {
        this.subElementRefEntries = subElementRefEntries;
    }


}