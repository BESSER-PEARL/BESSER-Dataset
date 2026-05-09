





import java.util.List;
import java.util.ArrayList;

public class Core_PhysicalElement  {

    private String path;
    private String isReadOnly;



    public Core_PhysicalElement(
        String path,        String isReadOnly    ) {
        this.path = path;
        this.isReadOnly = isReadOnly;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }


}