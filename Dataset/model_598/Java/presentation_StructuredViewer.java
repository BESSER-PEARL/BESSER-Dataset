





import java.util.List;
import java.util.ArrayList;

public class presentation_StructuredViewer extends ContentViewer {

    private String useHashlookup;
    private String group2;





    private List<presentation_IElementComparer> presentation_ielementcomparers;


    public presentation_StructuredViewer(
        String useHashlookup,        String group2    ) {
        super(
        );
        this.useHashlookup = useHashlookup;
        this.group2 = group2;
        this.presentation_ielementcomparers = new ArrayList<>();
    }

    public presentation_StructuredViewer(
        String useHashlookup,        String group2        ArrayList<presentation_IElementComparer> presentation_ielementcomparers    ) {
        this.useHashlookup = useHashlookup;
        this.group2 = group2;
        this.presentation_ielementcomparers = presentation_ielementcomparers;
    }

    public String getUsehashlookup() {
        return useHashlookup;
    }

    public void setUsehashlookup(String useHashlookup) {
        this.useHashlookup = useHashlookup;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }

    public List<presentation_IElementComparer> getPresentation_ielementcomparers() {
        return presentation_ielementcomparers;
    }

    public void addPresentation_ielementcomparer(Presentation_ielementcomparer presentation_ielementcomparer) {
        this.presentation_ielementcomparers.add(presentation_ielementcomparer);
    }

}