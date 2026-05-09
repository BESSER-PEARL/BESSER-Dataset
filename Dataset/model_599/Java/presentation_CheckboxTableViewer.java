





import java.util.List;
import java.util.ArrayList;

public class presentation_CheckboxTableViewer extends TableViewer {

    private String allGrayed;
    private String group5;
    private String allChecked;





    private List<presentation_EObject> presentation_eobjects;




    private List<presentation_EObject> presentation_eobjects;


    public presentation_CheckboxTableViewer(
        String allGrayed,        String group5,        String allChecked    ) {
        super(
        );
        this.allGrayed = allGrayed;
        this.group5 = group5;
        this.allChecked = allChecked;
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_CheckboxTableViewer(
        String allGrayed,        String group5,        String allChecked        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.allGrayed = allGrayed;
        this.group5 = group5;
        this.allChecked = allChecked;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_eobjects = presentation_eobjects;
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
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}