





import java.util.List;
import java.util.ArrayList;

public class presentation_ToolItem extends Item {

    private String toolTipText;
    private String selection;
    private String hotImage;
    private String bounds;
    private String disabledImage;
    private String group;
    private String enabled;
    private String width;





    private List<presentation_Control> presentation_controls;




    private List<presentation_ToolBar> presentation_toolbars;




    private presentation_ToolBar presentation_toolbar;


    public presentation_ToolItem(
        String toolTipText,        String selection,        String hotImage,        String bounds,        String disabledImage,        String group,        String enabled,        String width    ) {
        super(
        );
        this.toolTipText = toolTipText;
        this.selection = selection;
        this.hotImage = hotImage;
        this.bounds = bounds;
        this.disabledImage = disabledImage;
        this.group = group;
        this.enabled = enabled;
        this.width = width;
        this.presentation_controls = new ArrayList<>();
        this.presentation_toolbars = new ArrayList<>();
    }

    public presentation_ToolItem(
        String toolTipText,        String selection,        String hotImage,        String bounds,        String disabledImage,        String group,        String enabled,        String width        ArrayList<presentation_Control> presentation_controls,        ArrayList<presentation_ToolBar> presentation_toolbars    ) {
        this.toolTipText = toolTipText;
        this.selection = selection;
        this.hotImage = hotImage;
        this.bounds = bounds;
        this.disabledImage = disabledImage;
        this.group = group;
        this.enabled = enabled;
        this.width = width;
        this.presentation_controls = presentation_controls;
        this.presentation_toolbars = presentation_toolbars;
    }

    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getHotimage() {
        return hotImage;
    }

    public void setHotimage(String hotImage) {
        this.hotImage = hotImage;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }
    public String getDisabledimage() {
        return disabledImage;
    }

    public void setDisabledimage(String disabledImage) {
        this.disabledImage = disabledImage;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public List<presentation_ToolBar> getPresentation_toolbars() {
        return presentation_toolbars;
    }

    public void addPresentation_toolbar(Presentation_toolbar presentation_toolbar) {
        this.presentation_toolbars.add(presentation_toolbar);
    }
    public presentation_ToolBar getPresentation_toolbar() {
        return presentation_toolbar;
    }

    public void setPresentation_toolbar(presentation_ToolBar presentation_toolbar) {
        this.presentation_toolbar = presentation_toolbar;
    }

}