





import java.util.List;
import java.util.ArrayList;

public class lobj_Node  {

    private String id;
    private boolean visible;





    private lobj_Module lobj_module;


    public lobj_Node(
        String id,        boolean visible    ) {
        this.id = id;
        this.visible = visible;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public lobj_Module getLobj_module() {
        return lobj_module;
    }

    public void setLobj_module(lobj_Module lobj_module) {
        this.lobj_module = lobj_module;
    }

}