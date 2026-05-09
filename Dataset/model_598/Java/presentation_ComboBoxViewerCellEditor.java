





import java.util.List;
import java.util.ArrayList;

public class presentation_ComboBoxViewerCellEditor extends AbstractComboBoxCellEditor {

    private String group1;





    private List<presentation_IBaseLabelProvider> presentation_ibaselabelproviders;




    private List<presentation_ComboViewer> presentation_comboviewers;




    private List<presentation_EObject> presentation_eobjects;


    public presentation_ComboBoxViewerCellEditor(
        String group1    ) {
        super(
        );
        this.group1 = group1;
        this.presentation_ibaselabelproviders = new ArrayList<>();
        this.presentation_comboviewers = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_ComboBoxViewerCellEditor(
        String group1        ArrayList<presentation_IBaseLabelProvider> presentation_ibaselabelproviders,        ArrayList<presentation_ComboViewer> presentation_comboviewers,        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.group1 = group1;
        this.presentation_ibaselabelproviders = presentation_ibaselabelproviders;
        this.presentation_comboviewers = presentation_comboviewers;
        this.presentation_eobjects = presentation_eobjects;
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
    public List<presentation_ComboViewer> getPresentation_comboviewers() {
        return presentation_comboviewers;
    }

    public void addPresentation_comboviewer(Presentation_comboviewer presentation_comboviewer) {
        this.presentation_comboviewers.add(presentation_comboviewer);
    }
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}