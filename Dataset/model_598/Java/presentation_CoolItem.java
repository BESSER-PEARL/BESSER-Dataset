





import java.util.List;
import java.util.ArrayList;

public class presentation_CoolItem extends Item {

    private String size;
    private String minimumSize;
    private String preferredSize;
    private String group;
    private String bounds;





    private List<presentation_CoolBar> presentation_coolbars;




    private presentation_CoolBar presentation_coolbar;




    private List<presentation_Control> presentation_controls;


    public presentation_CoolItem(
        String size,        String minimumSize,        String preferredSize,        String group,        String bounds    ) {
        super(
        );
        this.size = size;
        this.minimumSize = minimumSize;
        this.preferredSize = preferredSize;
        this.group = group;
        this.bounds = bounds;
        this.presentation_coolbars = new ArrayList<>();
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_CoolItem(
        String size,        String minimumSize,        String preferredSize,        String group,        String bounds        ArrayList<presentation_CoolBar> presentation_coolbars,        ArrayList<presentation_Control> presentation_controls    ) {
        this.size = size;
        this.minimumSize = minimumSize;
        this.preferredSize = preferredSize;
        this.group = group;
        this.bounds = bounds;
        this.presentation_coolbars = presentation_coolbars;
        this.presentation_controls = presentation_controls;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getMinimumsize() {
        return minimumSize;
    }

    public void setMinimumsize(String minimumSize) {
        this.minimumSize = minimumSize;
    }
    public String getPreferredsize() {
        return preferredSize;
    }

    public void setPreferredsize(String preferredSize) {
        this.preferredSize = preferredSize;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
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
    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }

}