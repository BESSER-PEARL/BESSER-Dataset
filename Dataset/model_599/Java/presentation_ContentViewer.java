





import java.util.List;
import java.util.ArrayList;

public class presentation_ContentViewer extends Viewer {

    private String group1;





    private List<presentation_IBaseLabelProvider> presentation_ibaselabelproviders;


    public presentation_ContentViewer(
        String group1    ) {
        super(
        );
        this.group1 = group1;
        this.presentation_ibaselabelproviders = new ArrayList<>();
    }

    public presentation_ContentViewer(
        String group1        ArrayList<presentation_IBaseLabelProvider> presentation_ibaselabelproviders    ) {
        this.group1 = group1;
        this.presentation_ibaselabelproviders = presentation_ibaselabelproviders;
    }

    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }

    public List<presentation_IBaseLabelProvider> getPresentation_ibaselabelproviders() {
        return presentation_ibaselabelproviders;
    }

    public void addPresentation_ibaselabelprovider(Presentation_ibaselabelprovider presentation_ibaselabelprovider) {
        this.presentation_ibaselabelproviders.add(presentation_ibaselabelprovider);
    }

}