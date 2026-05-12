





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private None parent;
    private None name;
    private String id;
    private None section;



    public Category(
        None parent,        None name,        String id,        None section    ) {
        this.parent = parent;
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
    public None getSection() {
        return section;
    }

    public void setSection(None section) {
        this.section = section;
    }


}