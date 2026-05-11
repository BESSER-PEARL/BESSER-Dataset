





import java.util.List;
import java.util.ArrayList;

public class ed2_ED2  {

    private String name;





    private List<ed2_TreeElement> ed2_treeelements;


    public ed2_ED2(
        String name    ) {
        this.name = name;
        this.ed2_treeelements = new ArrayList<>();
    }

    public ed2_ED2(
        String name        ArrayList<ed2_TreeElement> ed2_treeelements    ) {
        this.name = name;
        this.ed2_treeelements = ed2_treeelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ed2_TreeElement> getEd2_treeelements() {
        return ed2_treeelements;
    }

    public void addEd2_treeelement(Ed2_treeelement ed2_treeelement) {
        this.ed2_treeelements.add(ed2_treeelement);
    }

}