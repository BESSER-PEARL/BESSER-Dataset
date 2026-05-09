





import java.util.List;
import java.util.ArrayList;

public class presentation_ICheckStateProvider  {

    private String mixed;





    private presentation_CheckboxTableViewer presentation_checkboxtableviewer;


    public presentation_ICheckStateProvider(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_CheckboxTableViewer getPresentation_checkboxtableviewer() {
        return presentation_checkboxtableviewer;
    }

    public void setPresentation_checkboxtableviewer(presentation_CheckboxTableViewer presentation_checkboxtableviewer) {
        this.presentation_checkboxtableviewer = presentation_checkboxtableviewer;
    }

}