





import java.util.List;
import java.util.ArrayList;

public class MocaTree_TreeElement  {

    private int index;
    private String name;





    private List<MocaTree_Link> mocatree_links;




    private MocaTree_Link mocatree_link;


    public MocaTree_TreeElement(
        int index,        String name    ) {
        this.index = index;
        this.name = name;
        this.mocatree_links = new ArrayList<>();
    }

    public MocaTree_TreeElement(
        int index,        String name        ArrayList<MocaTree_Link> mocatree_links    ) {
        this.index = index;
        this.name = name;
        this.mocatree_links = mocatree_links;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<MocaTree_Link> getMocatree_links() {
        return mocatree_links;
    }

    public void addMocatree_link(Mocatree_link mocatree_link) {
        this.mocatree_links.add(mocatree_link);
    }
    public MocaTree_Link getMocatree_link() {
        return mocatree_link;
    }

    public void setMocatree_link(MocaTree_Link mocatree_link) {
        this.mocatree_link = mocatree_link;
    }

}