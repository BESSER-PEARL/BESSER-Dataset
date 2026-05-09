





import java.util.List;
import java.util.ArrayList;

public class presentation_StackLayout extends Layout {

    private String group;
    private String marginWidth;
    private String marginHeight;





    private List<presentation_Control> presentation_controls;


    public presentation_StackLayout(
        String group,        String marginWidth,        String marginHeight    ) {
        super(
        );
        this.group = group;
        this.marginWidth = marginWidth;
        this.marginHeight = marginHeight;
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_StackLayout(
        String group,        String marginWidth,        String marginHeight        ArrayList<presentation_Control> presentation_controls    ) {
        this.group = group;
        this.marginWidth = marginWidth;
        this.marginHeight = marginHeight;
        this.presentation_controls = presentation_controls;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(String marginWidth) {
        this.marginWidth = marginWidth;
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