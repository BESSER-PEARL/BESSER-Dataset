





import java.util.List;
import java.util.ArrayList;

public class presentation_ControlEditor  {

    private String mixed;
    private String horizontalAlignment;
    private String group;
    private String minimumHeight;
    private String verticalAlignment;
    private String grabVertical;
    private String minimumWidth;
    private String grabHorizontal;





    private List<presentation_Control> presentation_controls;


    public presentation_ControlEditor(
        String mixed,        String horizontalAlignment,        String group,        String minimumHeight,        String verticalAlignment,        String grabVertical,        String minimumWidth,        String grabHorizontal    ) {
        this.mixed = mixed;
        this.horizontalAlignment = horizontalAlignment;
        this.group = group;
        this.minimumHeight = minimumHeight;
        this.verticalAlignment = verticalAlignment;
        this.grabVertical = grabVertical;
        this.minimumWidth = minimumWidth;
        this.grabHorizontal = grabHorizontal;
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_ControlEditor(
        String mixed,        String horizontalAlignment,        String group,        String minimumHeight,        String verticalAlignment,        String grabVertical,        String minimumWidth,        String grabHorizontal        ArrayList<presentation_Control> presentation_controls    ) {
        this.mixed = mixed;
        this.horizontalAlignment = horizontalAlignment;
        this.group = group;
        this.minimumHeight = minimumHeight;
        this.verticalAlignment = verticalAlignment;
        this.grabVertical = grabVertical;
        this.minimumWidth = minimumWidth;
        this.grabHorizontal = grabHorizontal;
        this.presentation_controls = presentation_controls;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMinimumheight() {
        return minimumHeight;
    }

    public void setMinimumheight(String minimumHeight) {
        this.minimumHeight = minimumHeight;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getGrabvertical() {
        return grabVertical;
    }

    public void setGrabvertical(String grabVertical) {
        this.grabVertical = grabVertical;
    }
    public String getMinimumwidth() {
        return minimumWidth;
    }

    public void setMinimumwidth(String minimumWidth) {
        this.minimumWidth = minimumWidth;
    }
    public String getGrabhorizontal() {
        return grabHorizontal;
    }

    public void setGrabhorizontal(String grabHorizontal) {
        this.grabHorizontal = grabHorizontal;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }

}