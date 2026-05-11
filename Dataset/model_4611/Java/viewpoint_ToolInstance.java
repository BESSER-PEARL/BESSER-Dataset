





import java.util.List;
import java.util.ArrayList;

public class viewpoint_ToolInstance  {

    private boolean enabled;
    private String id;
    private boolean filtered;
    private boolean visible;





    private viewpoint_ToolSectionInstance viewpoint_toolsectioninstance;


    public viewpoint_ToolInstance(
        boolean enabled,        String id,        boolean filtered,        boolean visible    ) {
        this.enabled = enabled;
        this.id = id;
        this.filtered = filtered;
        this.visible = visible;
    }


    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getFiltered() {
        return filtered;
    }

    public void setFiltered(boolean filtered) {
        this.filtered = filtered;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public viewpoint_ToolSectionInstance getViewpoint_toolsectioninstance() {
        return viewpoint_toolsectioninstance;
    }

    public void setViewpoint_toolsectioninstance(viewpoint_ToolSectionInstance viewpoint_toolsectioninstance) {
        this.viewpoint_toolsectioninstance = viewpoint_toolsectioninstance;
    }

}