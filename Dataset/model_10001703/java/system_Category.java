





import java.util.List;
import java.util.ArrayList;

public class system_Category  {

    private String icon;
    private String name;
    private None parent;
    private String section;
    private String id;



    public system_Category(
        String icon,        String name,        None parent,        String section,        String id    ) {
        this.icon = icon;
        this.name = name;
        this.parent = parent;
        this.section = section;
        this.id = id;
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
    public None getParent() {
        return parent;
    }

    public void setParent(None parent) {
        this.parent = parent;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}