





import java.util.List;
import java.util.ArrayList;

public class presentation_ControlEditor  {

    private String verticalAlignment;
    private String mixed;
    private String grabVertical;
    private String group;
    private String grabHorizontal;
    private String horizontalAlignment;
    private String minimumHeight;
    private String minimumWidth;





    private List<presentation_Control> presentation_controls;


    public presentation_ControlEditor(
        String verticalAlignment,        String mixed,        String grabVertical,        String group,        String grabHorizontal,        String horizontalAlignment,        String minimumHeight,        String minimumWidth    ) {
        this.verticalAlignment = verticalAlignment;
        this.mixed = mixed;
        this.grabVertical = grabVertical;
        this.group = group;
        this.grabHorizontal = grabHorizontal;
        this.horizontalAlignment = horizontalAlignment;
        this.minimumHeight = minimumHeight;
        this.minimumWidth = minimumWidth;
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_ControlEditor(
        String verticalAlignment,        String mixed,        String grabVertical,        String group,        String grabHorizontal,        String horizontalAlignment,        String minimumHeight,        String minimumWidth        ArrayList<presentation_Control> presentation_controls    ) {
        this.verticalAlignment = verticalAlignment;
        this.mixed = mixed;
        this.grabVertical = grabVertical;
        this.group = group;
        this.grabHorizontal = grabHorizontal;
        this.horizontalAlignment = horizontalAlignment;
        this.minimumHeight = minimumHeight;
        this.minimumWidth = minimumWidth;
        this.presentation_controls = presentation_controls;
    }

    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGrabvertical() {
        return grabVertical;
    }

    public void setGrabvertical(String grabVertical) {
        this.grabVertical = grabVertical;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getGrabhorizontal() {
        return grabHorizontal;
    }

    public void setGrabhorizontal(String grabHorizontal) {
        this.grabHorizontal = grabHorizontal;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getMinimumheight() {
        return minimumHeight;
    }

    public void setMinimumheight(String minimumHeight) {
        this.minimumHeight = minimumHeight;
    }
    public String getMinimumwidth() {
        return minimumWidth;
    }

    public void setMinimumwidth(String minimumWidth) {
        this.minimumWidth = minimumWidth;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }

}