





import java.util.List;
import java.util.ArrayList;

public class presentation_StackLayout extends Layout {

    private String marginWidth;
    private String group;
    private String marginHeight;





    private List<presentation_Control> presentation_controls;


    public presentation_StackLayout(
        String marginWidth,        String group,        String marginHeight    ) {
        super(
        );
        this.marginWidth = marginWidth;
        this.group = group;
        this.marginHeight = marginHeight;
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_StackLayout(
        String marginWidth,        String group,        String marginHeight        ArrayList<presentation_Control> presentation_controls    ) {
        this.marginWidth = marginWidth;
        this.group = group;
        this.marginHeight = marginHeight;
        this.presentation_controls = presentation_controls;
    }

    public String getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(String marginWidth) {
        this.marginWidth = marginWidth;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(String marginHeight) {
        this.marginHeight = marginHeight;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }

}