





import java.util.List;
import java.util.ArrayList;

public class presentation_ISelection  {

    private String mixed;





    private presentation_Viewer presentation_viewer;


    public presentation_ISelection(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_Viewer getPresentation_viewer() {
        return presentation_viewer;
    }

    public void setPresentation_viewer(presentation_Viewer presentation_viewer) {
        this.presentation_viewer = presentation_viewer;
    }

}