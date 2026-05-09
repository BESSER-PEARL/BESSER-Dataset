





import java.util.List;
import java.util.ArrayList;

public class presentation_ICellEditorValidator  {

    private String mixed;





    private presentation_CellEditor presentation_celleditor;


    public presentation_ICellEditorValidator(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_CellEditor getPresentation_celleditor() {
        return presentation_celleditor;
    }

    public void setPresentation_celleditor(presentation_CellEditor presentation_celleditor) {
        this.presentation_celleditor = presentation_celleditor;
    }

}