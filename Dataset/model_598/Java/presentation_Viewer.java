





import java.util.List;
import java.util.ArrayList;

public class presentation_Viewer  {

    private String group;
    private String mixed;





    private List<presentation_Control> presentation_controls;




    private List<presentation_ISelection> presentation_iselections;




    private List<presentation_EObject> presentation_eobjects;


    public presentation_Viewer(
        String group,        String mixed    ) {
        this.group = group;
        this.mixed = mixed;
        this.presentation_controls = new ArrayList<>();
        this.presentation_iselections = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_Viewer(
        String group,        String mixed        ArrayList<presentation_Control> presentation_controls,        ArrayList<presentation_ISelection> presentation_iselections,        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.group = group;
        this.mixed = mixed;
        this.presentation_controls = presentation_controls;
        this.presentation_iselections = presentation_iselections;
        this.presentation_eobjects = presentation_eobjects;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public List<presentation_ISelection> getPresentation_iselections() {
        return presentation_iselections;
    }

    public void addPresentation_iselection(Presentation_iselection presentation_iselection) {
        this.presentation_iselections.add(presentation_iselection);
    }
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}