





import java.util.List;
import java.util.ArrayList;

public class presentation_CheckboxTableViewer extends TableViewer {

    private String allChecked;
    private String allGrayed;
    private String group5;





    private List<presentation_EObject> presentation_eobjects;




    private List<presentation_EObject> presentation_eobjects;




    private List<presentation_ICheckStateProvider> presentation_icheckstateproviders;


    public presentation_CheckboxTableViewer(
        String allChecked,        String allGrayed,        String group5    ) {
        super(
        );
        this.allChecked = allChecked;
        this.allGrayed = allGrayed;
        this.group5 = group5;
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_icheckstateproviders = new ArrayList<>();
    }

    public presentation_CheckboxTableViewer(
        String allChecked,        String allGrayed,        String group5        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_ICheckStateProvider> presentation_icheckstateproviders    ) {
        this.allChecked = allChecked;
        this.allGrayed = allGrayed;
        this.group5 = group5;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_icheckstateproviders = presentation_icheckstateproviders;
    }

    public String getAllchecked() {
        return allChecked;
    }

    public void setAllchecked(String allChecked) {
        this.allChecked = allChecked;
    }
    public String getAllgrayed() {
        return allGrayed;
    }

    public void setAllgrayed(String allGrayed) {
        this.allGrayed = allGrayed;
    }
    public String getGroup5() {
        return group5;
    }

    public void setGroup5(String group5) {
        this.group5 = group5;
    }

    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
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

}