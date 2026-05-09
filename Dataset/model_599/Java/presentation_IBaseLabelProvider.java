





import java.util.List;
import java.util.ArrayList;

public class presentation_IBaseLabelProvider  {

    private String mixed;





    private presentation_ComboBoxViewerCellEditor presentation_comboboxviewercelleditor;


    public presentation_IBaseLabelProvider(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_ComboBoxViewerCellEditor getPresentation_comboboxviewercelleditor() {
        return presentation_comboboxviewercelleditor;
    }

    public void setPresentation_comboboxviewercelleditor(presentation_ComboBoxViewerCellEditor presentation_comboboxviewercelleditor) {
        this.presentation_comboboxviewercelleditor = presentation_comboboxviewercelleditor;
    }

}