





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String id;
    private None parent;
    private None section;
    private None name;



    public Category(
        String id,        None parent,        None section,        None name    ) {
        this.id = id;
        this.parent = parent;
        this.section = section;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getParent() {
        return parent;
    }

    public void setParent(None parent) {
        this.parent = parent;
    }
    public None getSection() {
        return section;
    }

    public void setSection(None section) {
        this.section = section;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }


}