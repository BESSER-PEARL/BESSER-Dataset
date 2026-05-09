





import java.util.List;
import java.util.ArrayList;

public class presentation_TabItem extends Item {

    private String toolTipText;
    private String group;
    private String bounds;





    private List<presentation_Control> presentation_controls;




    private presentation_TabFolder presentation_tabfolder;




    private List<presentation_TabFolder> presentation_tabfolders;




    private presentation_TabFolder presentation_tabfolder;


    public presentation_TabItem(
        String toolTipText,        String group,        String bounds    ) {
        super(
        );
        this.toolTipText = toolTipText;
        this.group = group;
        this.bounds = bounds;
        this.presentation_controls = new ArrayList<>();
        this.presentation_tabfolders = new ArrayList<>();
    }

    public presentation_TabItem(
        String toolTipText,        String group,        String bounds        ArrayList<presentation_Control> presentation_controls,        ArrayList<presentation_TabFolder> presentation_tabfolders    ) {
        this.toolTipText = toolTipText;
        this.group = group;
        this.bounds = bounds;
        this.presentation_controls = presentation_controls;
        this.presentation_tabfolders = presentation_tabfolders;
    }

    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
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

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public presentation_TabFolder getPresentation_tabfolder() {
        return presentation_tabfolder;
    }

    public void setPresentation_tabfolder(presentation_TabFolder presentation_tabfolder) {
        this.presentation_tabfolder = presentation_tabfolder;
    }
    public List<presentation_TabFolder> getPresentation_tabfolders() {
        return presentation_tabfolders;
    }

    public void addPresentation_tabfolder(Presentation_tabfolder presentation_tabfolder) {
        this.presentation_tabfolders.add(presentation_tabfolder);
    }
    public presentation_TabFolder getPresentation_tabfolder() {
        return presentation_tabfolder;
    }

    public void setPresentation_tabfolder(presentation_TabFolder presentation_tabfolder) {
        this.presentation_tabfolder = presentation_tabfolder;
    }

}