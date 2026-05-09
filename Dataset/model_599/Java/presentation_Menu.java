





import java.util.List;
import java.util.ArrayList;

public class presentation_Menu extends Widget {

    private String visible;
    private String enabled;
    private String handle;
    private String group;





    private List<presentation_Menu> presentation_menus;


    public presentation_Menu(
        String visible,        String enabled,        String handle,        String group    ) {
        super(
        );
        this.visible = visible;
        this.enabled = enabled;
        this.handle = handle;
        this.group = group;
        this.presentation_menus = new ArrayList<>();
    }

    public presentation_Menu(
        String visible,        String enabled,        String handle,        String group        ArrayList<presentation_Menu> presentation_menus    ) {
        this.visible = visible;
        this.enabled = enabled;
        this.handle = handle;
        this.group = group;
        this.presentation_menus = presentation_menus;
    }

    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getHandle() {
        return handle;
    }

    public void setHandle(String handle) {
        this.handle = handle;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<presentation_Menu> getPresentation_menus() {
        return presentation_menus;
    }

    public void addPresentation_menu(Presentation_menu presentation_menu) {
        this.presentation_menus.add(presentation_menu);
    }

}