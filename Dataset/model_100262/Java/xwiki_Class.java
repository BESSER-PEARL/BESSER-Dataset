





import java.util.List;
import java.util.ArrayList;

public class xwiki_Class extends LinkCollection {

    private String id;
    private String name;





    private xwiki_ClassesType xwiki_classestype;


    public xwiki_Class(
        String id,        String name    ) {
        super(
        );
        this.id = id;
        this.name = name;
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

    public xwiki_ClassesType getXwiki_classestype() {
        return xwiki_classestype;
    }

    public void setXwiki_classestype(xwiki_ClassesType xwiki_classestype) {
        this.xwiki_classestype = xwiki_classestype;
    }

}