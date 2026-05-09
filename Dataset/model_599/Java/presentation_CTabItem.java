





import java.util.List;
import java.util.ArrayList;

public class presentation_CTabItem extends Item {

    private String bounds;
    private String group;
    private String toolTipText;
    private String showClose;
    private String disabledImage;
    private String font;





    private presentation_CTabFolder presentation_ctabfolder;




    private List<presentation_Control> presentation_controls;




    private List<presentation_CTabFolder> presentation_ctabfolders;




    private presentation_CTabFolder presentation_ctabfolder;


    public presentation_CTabItem(
        String bounds,        String group,        String toolTipText,        String showClose,        String disabledImage,        String font    ) {
        super(
        );
        this.bounds = bounds;
        this.group = group;
        this.toolTipText = toolTipText;
        this.showClose = showClose;
        this.disabledImage = disabledImage;
        this.font = font;
        this.presentation_controls = new ArrayList<>();
        this.presentation_ctabfolders = new ArrayList<>();
    }

    public presentation_CTabItem(
        String bounds,        String group,        String toolTipText,        String showClose,        String disabledImage,        String font        ArrayList<presentation_Control> presentation_controls,        ArrayList<presentation_CTabFolder> presentation_ctabfolders    ) {
        this.bounds = bounds;
        this.group = group;
        this.toolTipText = toolTipText;
        this.showClose = showClose;
        this.disabledImage = disabledImage;
        this.font = font;
        this.presentation_controls = presentation_controls;
        this.presentation_ctabfolders = presentation_ctabfolders;
    }

    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public String getShowclose() {
        return showClose;
    }

    public void setShowclose(String showClose) {
        this.showClose = showClose;
    }
    public String getDisabledimage() {
        return disabledImage;
    }

    public void setDisabledimage(String disabledImage) {
        this.disabledImage = disabledImage;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }

    public presentation_CTabFolder getPresentation_ctabfolder() {
        return presentation_ctabfolder;
    }

    public void setPresentation_ctabfolder(presentation_CTabFolder presentation_ctabfolder) {
        this.presentation_ctabfolder = presentation_ctabfolder;
    }
    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public List<presentation_CTabFolder> getPresentation_ctabfolders() {
        return presentation_ctabfolders;
    }

    public void addPresentation_ctabfolder(Presentation_ctabfolder presentation_ctabfolder) {
        this.presentation_ctabfolders.add(presentation_ctabfolder);
    }
    public presentation_CTabFolder getPresentation_ctabfolder() {
        return presentation_ctabfolder;
    }

    public void setPresentation_ctabfolder(presentation_CTabFolder presentation_ctabfolder) {
        this.presentation_ctabfolder = presentation_ctabfolder;
    }

}