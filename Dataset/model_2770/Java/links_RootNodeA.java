





import java.util.List;
import java.util.ArrayList;

public class links_RootNodeA  {






    private links_Root_BA_Element_Link links_root_ba_element_link;




    private List<links_ChildNodeA> links_childnodeas;




    private links_RootNodeB links_rootnodeb;




    private links_Root links_root;


    public links_RootNodeA(
    ) {
        this.links_childnodeas = new ArrayList<>();
    }

    public links_RootNodeA(
        ArrayList<links_ChildNodeA> links_childnodeas    ) {
        this.links_childnodeas = links_childnodeas;
    }


    public links_Root_BA_Element_Link getLinks_root_ba_element_link() {
        return links_root_ba_element_link;
    }

    public void setLinks_root_ba_element_link(links_Root_BA_Element_Link links_root_ba_element_link) {
        this.links_root_ba_element_link = links_root_ba_element_link;
    }
    public List<links_ChildNodeA> getLinks_childnodeas() {
        return links_childnodeas;
    }

    public void addLinks_childnodea(Links_childnodea links_childnodea) {
        this.links_childnodeas.add(links_childnodea);
    }
    public links_RootNodeB getLinks_rootnodeb() {
        return links_rootnodeb;
    }

    public void setLinks_rootnodeb(links_RootNodeB links_rootnodeb) {
        this.links_rootnodeb = links_rootnodeb;
    }
    public links_Root getLinks_root() {
        return links_root;
    }

    public void setLinks_root(links_Root links_root) {
        this.links_root = links_root;
    }

}