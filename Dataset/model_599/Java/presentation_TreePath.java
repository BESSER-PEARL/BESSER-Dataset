





import java.util.List;
import java.util.ArrayList;

public class presentation_TreePath  {

    private String mixed;





    private presentation_AbstractTreeViewer presentation_abstracttreeviewer;


    public presentation_TreePath(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_AbstractTreeViewer getPresentation_abstracttreeviewer() {
        return presentation_abstracttreeviewer;
    }

    public void setPresentation_abstracttreeviewer(presentation_AbstractTreeViewer presentation_abstracttreeviewer) {
        this.presentation_abstracttreeviewer = presentation_abstracttreeviewer;
    }

}