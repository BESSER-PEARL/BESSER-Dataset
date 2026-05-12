





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private None parent;
    private None section;
    private None name;
    private String id;



    public Category(
        None parent,        None section,        None name,        String id    ) {
        this.parent = parent;
        this.section = section;
        this.name = name;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}