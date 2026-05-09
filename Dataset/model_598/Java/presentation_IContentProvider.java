





import java.util.List;
import java.util.ArrayList;

public class presentation_IContentProvider  {

    private String mixed;





    private presentation_ContentViewer presentation_contentviewer;


    public presentation_IContentProvider(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_ContentViewer getPresentation_contentviewer() {
        return presentation_contentviewer;
    }

    public void setPresentation_contentviewer(presentation_ContentViewer presentation_contentviewer) {
        this.presentation_contentviewer = presentation_contentviewer;
    }

}