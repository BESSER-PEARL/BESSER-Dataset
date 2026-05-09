





import java.util.List;
import java.util.ArrayList;

public class Core_PhysicalElement  {

    private String isReadOnly;
    private String path;



    public Core_PhysicalElement(
        String isReadOnly,        String path    ) {
        this.isReadOnly = isReadOnly;
        this.path = path;
    }


    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}