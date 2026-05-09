





import java.util.List;
import java.util.ArrayList;

public class presentation_StructuredViewer extends ContentViewer {

    private String group2;
    private String useHashlookup;





    private List<presentation_ViewerFilter> presentation_viewerfilters;




    private List<presentation_IElementComparer> presentation_ielementcomparers;




    private List<presentation_ViewerSorter> presentation_viewersorters;


    public presentation_StructuredViewer(
        String group2,        String useHashlookup    ) {
        super(
        );
        this.group2 = group2;
        this.useHashlookup = useHashlookup;
        this.presentation_viewerfilters = new ArrayList<>();
        this.presentation_ielementcomparers = new ArrayList<>();
        this.presentation_viewersorters = new ArrayList<>();
    }

    public presentation_StructuredViewer(
        String group2,        String useHashlookup        ArrayList<presentation_ViewerFilter> presentation_viewerfilters,        ArrayList<presentation_IElementComparer> presentation_ielementcomparers,        ArrayList<presentation_ViewerSorter> presentation_viewersorters    ) {
        this.group2 = group2;
        this.useHashlookup = useHashlookup;
        this.presentation_viewerfilters = presentation_viewerfilters;
        this.presentation_ielementcomparers = presentation_ielementcomparers;
        this.presentation_viewersorters = presentation_viewersorters;
    }

    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getUsehashlookup() {
        return useHashlookup;
    }

    public void setUsehashlookup(String useHashlookup) {
        this.useHashlookup = useHashlookup;
    }

    public List<presentation_ViewerFilter> getPresentation_viewerfilters() {
        return presentation_viewerfilters;
    }

    public void addPresentation_viewerfilter(Presentation_viewerfilter presentation_viewerfilter) {
        this.presentation_viewerfilters.add(presentation_viewerfilter);
    }
    public List<presentation_IElementComparer> getPresentation_ielementcomparers() {
        return presentation_ielementcomparers;
    }

    public void addPresentation_ielementcomparer(Presentation_ielementcomparer presentation_ielementcomparer) {
        this.presentation_ielementcomparers.add(presentation_ielementcomparer);
    }
    public List<presentation_ViewerSorter> getPresentation_viewersorters() {
        return presentation_viewersorters;
    }

    public void addPresentation_viewersorter(Presentation_viewersorter presentation_viewersorter) {
        this.presentation_viewersorters.add(presentation_viewersorter);
    }

}