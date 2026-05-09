





import java.util.List;
import java.util.ArrayList;

public class presentation_Dialog extends Window {

    private String group1;





    private List<presentation_Control> presentation_controls;


    public presentation_Dialog(
        String group1    ) {
        super(
        );
        this.group1 = group1;
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_Dialog(
        String group1        ArrayList<presentation_Control> presentation_controls    ) {
        this.group1 = group1;
        this.presentation_controls = presentation_controls;
    }

    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }

}