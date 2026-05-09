





import java.util.List;
import java.util.ArrayList;

public class presentation_Composite extends Scrollable {

    private String layoutDeferred;
    private String backgroundMode;
    private String group2;





    private List<presentation_Control> presentation_controls;




    private List<presentation_Control> presentation_controls;


    public presentation_Composite(
        String layoutDeferred,        String backgroundMode,        String group2    ) {
        super(
        );
        this.layoutDeferred = layoutDeferred;
        this.backgroundMode = backgroundMode;
        this.group2 = group2;
        this.presentation_controls = new ArrayList<>();
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_Composite(
        String layoutDeferred,        String backgroundMode,        String group2        ArrayList<presentation_Control> presentation_controls,        ArrayList<presentation_Control> presentation_controls    ) {
        this.layoutDeferred = layoutDeferred;
        this.backgroundMode = backgroundMode;
        this.group2 = group2;
        this.presentation_controls = presentation_controls;
        this.presentation_controls = presentation_controls;
    }

    public String getLayoutdeferred() {
        return layoutDeferred;
    }

    public void setLayoutdeferred(String layoutDeferred) {
        this.layoutDeferred = layoutDeferred;
    }
    public String getBackgroundmode() {
        return backgroundMode;
    }

    public void setBackgroundmode(String backgroundMode) {
        this.backgroundMode = backgroundMode;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }

}