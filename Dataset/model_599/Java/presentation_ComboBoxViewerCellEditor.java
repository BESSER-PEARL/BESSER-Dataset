





import java.util.List;
import java.util.ArrayList;

public class presentation_ComboBoxViewerCellEditor extends AbstractComboBoxCellEditor {

    private String group1;





    private List<presentation_EObject> presentation_eobjects;


    public presentation_ComboBoxViewerCellEditor(
        String group1    ) {
        super(
        );
        this.group1 = group1;
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_ComboBoxViewerCellEditor(
        String group1        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.group1 = group1;
        this.presentation_eobjects = presentation_eobjects;
    }

    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }

    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}