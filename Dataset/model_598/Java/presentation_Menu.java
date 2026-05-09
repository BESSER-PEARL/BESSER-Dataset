





import java.util.List;
import java.util.ArrayList;

public class presentation_Menu extends Widget {

    private String enabled;
    private String handle;
    private String visible;
    private String group;





    private presentation_Menu presentation_menu;


    public presentation_Menu(
        String enabled,        String handle,        String visible,        String group    ) {
        super(
        );
        this.enabled = enabled;
        this.handle = handle;
        this.visible = visible;
        this.group = group;
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
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public presentation_Menu getPresentation_menu() {
        return presentation_menu;
    }

    public void setPresentation_menu(presentation_Menu presentation_menu) {
        this.presentation_menu = presentation_menu;
    }

}