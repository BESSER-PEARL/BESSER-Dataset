





import java.util.List;
import java.util.ArrayList;

public class HSVTree_HSVNode  {

    private String hsv;
    private String name;





    private List<HSVTree_HSVNode> hsvtree_hsvnodes;




    private HSVTree_HSVNode hsvtree_hsvnode;


    public HSVTree_HSVNode(
        String hsv,        String name    ) {
        this.hsv = hsv;
        this.name = name;
        this.hsvtree_hsvnodes = new ArrayList<>();
    }

    public HSVTree_HSVNode(
        String hsv,        String name        ArrayList<HSVTree_HSVNode> hsvtree_hsvnodes    ) {
        this.hsv = hsv;
        this.name = name;
        this.hsvtree_hsvnodes = hsvtree_hsvnodes;
    }

    public String getHsv() {
        return hsv;
    }

    public void setHsv(String hsv) {
        this.hsv = hsv;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<HSVTree_HSVNode> getHsvtree_hsvnodes() {
        return hsvtree_hsvnodes;
    }

    public void addHsvtree_hsvnode(Hsvtree_hsvnode hsvtree_hsvnode) {
        this.hsvtree_hsvnodes.add(hsvtree_hsvnode);
    }
    public HSVTree_HSVNode getHsvtree_hsvnode() {
        return hsvtree_hsvnode;
    }

    public void setHsvtree_hsvnode(HSVTree_HSVNode hsvtree_hsvnode) {
        this.hsvtree_hsvnode = hsvtree_hsvnode;
    }

}