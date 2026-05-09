





import java.util.List;
import java.util.ArrayList;

public class presentation_ICellModifier  {

    private String mixed;





    private presentation_ColumnViewer presentation_columnviewer;


    public presentation_ICellModifier(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_ColumnViewer getPresentation_columnviewer() {
        return presentation_columnviewer;
    }

    public void setPresentation_columnviewer(presentation_ColumnViewer presentation_columnviewer) {
        this.presentation_columnviewer = presentation_columnviewer;
    }

}