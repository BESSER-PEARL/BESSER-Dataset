





import java.util.List;
import java.util.ArrayList;

public class presentation_CTabItem extends Item {

    private String group;
    private String disabledImage;
    private String showClose;
    private String toolTipText;
    private String font;
    private String bounds;





    private presentation_CTabFolder presentation_ctabfolder;




    private presentation_CTabFolder presentation_ctabfolder;




    private List<presentation_Control> presentation_controls;




    private List<presentation_CTabFolder> presentation_ctabfolders;


    public presentation_CTabItem(
        String group,        String disabledImage,        String showClose,        String toolTipText,        String font,        String bounds    ) {
        super(
        );
        this.group = group;
        this.disabledImage = disabledImage;
        this.showClose = showClose;
        this.toolTipText = toolTipText;
        this.font = font;
        this.bounds = bounds;
        this.presentation_controls = new ArrayList<>();
        this.presentation_ctabfolders = new ArrayList<>();
    }

    public presentation_CTabItem(
        String group,        String disabledImage,        String showClose,        String toolTipText,        String font,        String bounds        ArrayList<presentation_Control> presentation_controls,        ArrayList<presentation_CTabFolder> presentation_ctabfolders    ) {
        this.group = group;
        this.disabledImage = disabledImage;
        this.showClose = showClose;
        this.toolTipText = toolTipText;
        this.font = font;
        this.bounds = bounds;
        this.presentation_controls = presentation_controls;
        this.presentation_ctabfolders = presentation_ctabfolders;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getDisabledimage() {
        return disabledImage;
    }

    public void setDisabledimage(String disabledImage) {
        this.disabledImage = disabledImage;
    }
    public String getShowclose() {
        return showClose;
    }

    public void setShowclose(String showClose) {
        this.showClose = showClose;
    }
    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }

    public presentation_CTabFolder getPresentation_ctabfolder() {
        return presentation_ctabfolder;
    }

    public void setPresentation_ctabfolder(presentation_CTabFolder presentation_ctabfolder) {
        this.presentation_ctabfolder = presentation_ctabfolder;
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

}