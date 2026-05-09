





import java.util.List;
import java.util.ArrayList;

public class presentation_ExpandItem extends Item {

    private String group;
    private String height;
    private String expanded;





    private List<presentation_ExpandBar> presentation_expandbars;




    private List<presentation_Control> presentation_controls;




    private presentation_ExpandBar presentation_expandbar;


    public presentation_ExpandItem(
        String group,        String height,        String expanded    ) {
        super(
        );
        this.group = group;
        this.height = height;
        this.expanded = expanded;
        this.presentation_expandbars = new ArrayList<>();
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_ExpandItem(
        String group,        String height,        String expanded        ArrayList<presentation_ExpandBar> presentation_expandbars,        ArrayList<presentation_Control> presentation_controls    ) {
        this.group = group;
        this.height = height;
        this.expanded = expanded;
        this.presentation_expandbars = presentation_expandbars;
        this.presentation_controls = presentation_controls;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getExpanded() {
        return expanded;
    }

    public void setExpanded(String expanded) {
        this.expanded = expanded;
    }

    public List<presentation_ExpandBar> getPresentation_expandbars() {
        return presentation_expandbars;
    }

    public void addPresentation_expandbar(Presentation_expandbar presentation_expandbar) {
        this.presentation_expandbars.add(presentation_expandbar);
    }
    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public presentation_ExpandBar getPresentation_expandbar() {
        return presentation_expandbar;
    }

    public void setPresentation_expandbar(presentation_ExpandBar presentation_expandbar) {
        this.presentation_expandbar = presentation_expandbar;
    }

}