





import java.util.List;
import java.util.ArrayList;

public class system_Category  {

    private None parent;
    private String icon;
    private String name;
    private String id;
    private String section;



    public system_Category(
        None parent,        String icon,        String name,        String id,        String section    ) {
        this.parent = parent;
        this.icon = icon;
        this.name = name;
        this.id = id;
        this.section = section;
    }


    public None getParent() {
        return parent;
    }

    public void setParent(None parent) {
        this.parent = parent;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }


}