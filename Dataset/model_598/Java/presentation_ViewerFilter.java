





import java.util.List;
import java.util.ArrayList;

public class presentation_ViewerFilter  {

    private String mixed;





    private presentation_StructuredViewer presentation_structuredviewer;


    public presentation_ViewerFilter(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_StructuredViewer getPresentation_structuredviewer() {
        return presentation_structuredviewer;
    }

    public void setPresentation_structuredviewer(presentation_StructuredViewer presentation_structuredviewer) {
        this.presentation_structuredviewer = presentation_structuredviewer;
    }

}