





import java.util.List;
import java.util.ArrayList;

public class ed2_EDD  {

    private String name;





    private List<ed2_TreeObject> ed2_treeobjects;




    private List<ed2_TreeParent> ed2_treeparents;


    public ed2_EDD(
        String name    ) {
        this.name = name;
        this.ed2_treeobjects = new ArrayList<>();
        this.ed2_treeparents = new ArrayList<>();
    }

    public ed2_EDD(
        String name        ArrayList<ed2_TreeObject> ed2_treeobjects,        ArrayList<ed2_TreeParent> ed2_treeparents    ) {
        this.name = name;
        this.ed2_treeobjects = ed2_treeobjects;
        this.ed2_treeparents = ed2_treeparents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ed2_TreeObject> getEd2_treeobjects() {
        return ed2_treeobjects;
    }

    public void addEd2_treeobject(Ed2_treeobject ed2_treeobject) {
        this.ed2_treeobjects.add(ed2_treeobject);
    }
    public List<ed2_TreeParent> getEd2_treeparents() {
        return ed2_treeparents;
    }

    public void addEd2_treeparent(Ed2_treeparent ed2_treeparent) {
        this.ed2_treeparents.add(ed2_treeparent);
    }

}