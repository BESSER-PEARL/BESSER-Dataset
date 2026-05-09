





import java.util.List;
import java.util.ArrayList;

public class presentation_CoolItem extends Item {

    private String minimumSize;
    private String group;
    private String preferredSize;
    private String size;
    private String bounds;





    private List<presentation_Control> presentation_controls;




    private List<presentation_CoolBar> presentation_coolbars;




    private presentation_CoolBar presentation_coolbar;


    public presentation_CoolItem(
        String minimumSize,        String group,        String preferredSize,        String size,        String bounds    ) {
        super(
        );
        this.minimumSize = minimumSize;
        this.group = group;
        this.preferredSize = preferredSize;
        this.size = size;
        this.bounds = bounds;
        this.presentation_controls = new ArrayList<>();
        this.presentation_coolbars = new ArrayList<>();
    }

    public presentation_CoolItem(
        String minimumSize,        String group,        String preferredSize,        String size,        String bounds        ArrayList<presentation_Control> presentation_controls,        ArrayList<presentation_CoolBar> presentation_coolbars    ) {
        this.minimumSize = minimumSize;
        this.group = group;
        this.preferredSize = preferredSize;
        this.size = size;
        this.bounds = bounds;
        this.presentation_controls = presentation_controls;
        this.presentation_coolbars = presentation_coolbars;
    }

    public String getMinimumsize() {
        return minimumSize;
    }

    public void setMinimumsize(String minimumSize) {
        this.minimumSize = minimumSize;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getPreferredsize() {
        return preferredSize;
    }

    public void setPreferredsize(String preferredSize) {
        this.preferredSize = preferredSize;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public List<presentation_CoolBar> getPresentation_coolbars() {
        return presentation_coolbars;
    }

    public void addPresentation_coolbar(Presentation_coolbar presentation_coolbar) {
        this.presentation_coolbars.add(presentation_coolbar);
    }
    public presentation_CoolBar getPresentation_coolbar() {
        return presentation_coolbar;
    }

    public void setPresentation_coolbar(presentation_CoolBar presentation_coolbar) {
        this.presentation_coolbar = presentation_coolbar;
    }

}