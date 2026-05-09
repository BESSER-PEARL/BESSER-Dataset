





import java.util.List;
import java.util.ArrayList;

public class presentation_Control extends Widget {

    private String location;
    private String handle;
    private String enabled;
    private String backgroundImage;
    private String dragDetect;
    private String capture;
    private String background;
    private String toolTipText;
    private String foreground;
    private String redraw;
    private String visible;
    private String bounds;
    private String group;
    private String size;
    private String font;





    private presentation_Viewer presentation_viewer;




    private presentation_CTabFolder presentation_ctabfolder;




    private List<presentation_Accessible> presentation_accessibles;




    private List<presentation_EObject> presentation_eobjects;




    private presentation_SashForm presentation_sashform;




    private List<presentation_Menu> presentation_menus;


    public presentation_Control(
        String location,        String handle,        String enabled,        String backgroundImage,        String dragDetect,        String capture,        String background,        String toolTipText,        String foreground,        String redraw,        String visible,        String bounds,        String group,        String size,        String font    ) {
        super(
        );
        this.location = location;
        this.handle = handle;
        this.enabled = enabled;
        this.backgroundImage = backgroundImage;
        this.dragDetect = dragDetect;
        this.capture = capture;
        this.background = background;
        this.toolTipText = toolTipText;
        this.foreground = foreground;
        this.redraw = redraw;
        this.visible = visible;
        this.bounds = bounds;
        this.group = group;
        this.size = size;
        this.font = font;
        this.presentation_accessibles = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_menus = new ArrayList<>();
    }

    public presentation_Control(
        String location,        String handle,        String enabled,        String backgroundImage,        String dragDetect,        String capture,        String background,        String toolTipText,        String foreground,        String redraw,        String visible,        String bounds,        String group,        String size,        String font        ArrayList<presentation_Accessible> presentation_accessibles,        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_Menu> presentation_menus    ) {
        this.location = location;
        this.handle = handle;
        this.enabled = enabled;
        this.backgroundImage = backgroundImage;
        this.dragDetect = dragDetect;
        this.capture = capture;
        this.background = background;
        this.toolTipText = toolTipText;
        this.foreground = foreground;
        this.redraw = redraw;
        this.visible = visible;
        this.bounds = bounds;
        this.group = group;
        this.size = size;
        this.font = font;
        this.presentation_accessibles = presentation_accessibles;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_menus = presentation_menus;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getHandle() {
        return handle;
    }

    public void setHandle(String handle) {
        this.handle = handle;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getBackgroundimage() {
        return backgroundImage;
    }

    public void setBackgroundimage(String backgroundImage) {
        this.backgroundImage = backgroundImage;
    }
    public String getDragdetect() {
        return dragDetect;
    }

    public void setDragdetect(String dragDetect) {
        this.dragDetect = dragDetect;
    }
    public String getCapture() {
        return capture;
    }

    public void setCapture(String capture) {
        this.capture = capture;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public String getForeground() {
        return foreground;
    }

    public void setForeground(String foreground) {
        this.foreground = foreground;
    }
    public String getRedraw() {
        return redraw;
    }

    public void setRedraw(String redraw) {
        this.redraw = redraw;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
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
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }

    public presentation_Viewer getPresentation_viewer() {
        return presentation_viewer;
    }

    public void setPresentation_viewer(presentation_Viewer presentation_viewer) {
        this.presentation_viewer = presentation_viewer;
    }
    public presentation_CTabFolder getPresentation_ctabfolder() {
        return presentation_ctabfolder;
    }

    public void setPresentation_ctabfolder(presentation_CTabFolder presentation_ctabfolder) {
        this.presentation_ctabfolder = presentation_ctabfolder;
    }
    public List<presentation_Accessible> getPresentation_accessibles() {
        return presentation_accessibles;
    }

    public void addPresentation_accessible(Presentation_accessible presentation_accessible) {
        this.presentation_accessibles.add(presentation_accessible);
    }
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }
    public presentation_SashForm getPresentation_sashform() {
        return presentation_sashform;
    }

    public void setPresentation_sashform(presentation_SashForm presentation_sashform) {
        this.presentation_sashform = presentation_sashform;
    }
    public List<presentation_Menu> getPresentation_menus() {
        return presentation_menus;
    }

    public void addPresentation_menu(Presentation_menu presentation_menu) {
        this.presentation_menus.add(presentation_menu);
    }

}