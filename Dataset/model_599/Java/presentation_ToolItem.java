





import java.util.List;
import java.util.ArrayList;

public class presentation_ToolItem extends Item {

    private String disabledImage;
    private String enabled;
    private String group;
    private String width;
    private String bounds;
    private String hotImage;
    private String selection;
    private String toolTipText;





    private List<presentation_ToolBar> presentation_toolbars;




    private List<presentation_Control> presentation_controls;




    private presentation_ToolBar presentation_toolbar;


    public presentation_ToolItem(
        String disabledImage,        String enabled,        String group,        String width,        String bounds,        String hotImage,        String selection,        String toolTipText    ) {
        super(
        );
        this.disabledImage = disabledImage;
        this.enabled = enabled;
        this.group = group;
        this.width = width;
        this.bounds = bounds;
        this.hotImage = hotImage;
        this.selection = selection;
        this.toolTipText = toolTipText;
        this.presentation_toolbars = new ArrayList<>();
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_ToolItem(
        String disabledImage,        String enabled,        String group,        String width,        String bounds,        String hotImage,        String selection,        String toolTipText        ArrayList<presentation_ToolBar> presentation_toolbars,        ArrayList<presentation_Control> presentation_controls    ) {
        this.disabledImage = disabledImage;
        this.enabled = enabled;
        this.group = group;
        this.width = width;
        this.bounds = bounds;
        this.hotImage = hotImage;
        this.selection = selection;
        this.toolTipText = toolTipText;
        this.presentation_toolbars = presentation_toolbars;
        this.presentation_controls = presentation_controls;
    }

    public String getDisabledimage() {
        return disabledImage;
    }

    public void setDisabledimage(String disabledImage) {
        this.disabledImage = disabledImage;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }
    public String getHotimage() {
        return hotImage;
    }

    public void setHotimage(String hotImage) {
        this.hotImage = hotImage;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }

    public List<presentation_ToolBar> getPresentation_toolbars() {
        return presentation_toolbars;
    }

    public void addPresentation_toolbar(Presentation_toolbar presentation_toolbar) {
        this.presentation_toolbars.add(presentation_toolbar);
    }
    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public presentation_ToolBar getPresentation_toolbar() {
        return presentation_toolbar;
    }

    public void setPresentation_toolbar(presentation_ToolBar presentation_toolbar) {
        this.presentation_toolbar = presentation_toolbar;
    }

}