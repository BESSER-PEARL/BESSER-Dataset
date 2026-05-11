





import java.util.List;
import java.util.ArrayList;

public class ed2_TreeParent  {

    private String name;
    private String index;
    private String type;





    private List<ed2_TreeObject> ed2_treeobjects;




    private ed2_TreeParent ed2_treeparent;


    public ed2_TreeParent(
        String name,        String index,        String type    ) {
        this.name = name;
        this.index = index;
        this.type = type;
        this.ed2_treeobjects = new ArrayList<>();
    }

    public ed2_TreeParent(
        String name,        String index,        String type        ArrayList<ed2_TreeObject> ed2_treeobjects    ) {
        this.name = name;
        this.index = index;
        this.type = type;
        this.ed2_treeobjects = ed2_treeobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<ed2_TreeObject> getEd2_treeobjects() {
        return ed2_treeobjects;
    }

    public void addEd2_treeobject(Ed2_treeobject ed2_treeobject) {
        this.ed2_treeobjects.add(ed2_treeobject);
    }
    public ed2_TreeParent getEd2_treeparent() {
        return ed2_treeparent;
    }

    public void setEd2_treeparent(ed2_TreeParent ed2_treeparent) {
        this.ed2_treeparent = ed2_treeparent;
    }

}