





import java.util.List;
import java.util.ArrayList;

public class system_Category  {

    private String icon;
    private String id;
    private String name;
    private String section;
    private None parent;



    public system_Category(
        String icon,        String id,        String name,        String section,        None parent    ) {
        this.icon = icon;
        this.id = id;
        this.name = name;
        this.section = section;
        this.parent = parent;
    }


    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public None getParent() {
        return parent;
    }

    public void setParent(None parent) {
        this.parent = parent;
    }


}