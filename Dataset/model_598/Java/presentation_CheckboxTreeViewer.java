





import java.util.List;
import java.util.ArrayList;

public class presentation_CheckboxTreeViewer extends TreeViewer {

    private String group6;
    private String allChecked;





    private List<presentation_EObject> presentation_eobjects;




    private List<presentation_ICheckStateProvider> presentation_icheckstateproviders;




    private List<presentation_EObject> presentation_eobjects;


    public presentation_CheckboxTreeViewer(
        String group6,        String allChecked    ) {
        super(
        );
        this.group6 = group6;
        this.allChecked = allChecked;
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_icheckstateproviders = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_CheckboxTreeViewer(
        String group6,        String allChecked        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_ICheckStateProvider> presentation_icheckstateproviders,        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.group6 = group6;
        this.allChecked = allChecked;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_icheckstateproviders = presentation_icheckstateproviders;
        this.presentation_eobjects = presentation_eobjects;
    }

    public String getGroup6() {
        return group6;
    }

    public void setGroup6(String group6) {
        this.group6 = group6;
    }
    public String getAllchecked() {
        return allChecked;
    }

    public void setAllchecked(String allChecked) {
        this.allChecked = allChecked;
    }

    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }
    public List<presentation_ICheckStateProvider> getPresentation_icheckstateproviders() {
        return presentation_icheckstateproviders;
    }

    public void addPresentation_icheckstateprovider(Presentation_icheckstateprovider presentation_icheckstateprovider) {
        this.presentation_icheckstateproviders.add(presentation_icheckstateprovider);
    }
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}