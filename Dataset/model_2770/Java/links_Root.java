





import java.util.List;
import java.util.ArrayList;

public class links_Root  {






    private List<links_Root_BA_Element_Link> links_root_ba_element_links;




    private List<links_RootNodeB> links_rootnodebs;


    public links_Root(
    ) {
        this.links_root_ba_element_links = new ArrayList<>();
        this.links_rootnodebs = new ArrayList<>();
    }

    public links_Root(
        ArrayList<links_Root_BA_Element_Link> links_root_ba_element_links,        ArrayList<links_RootNodeB> links_rootnodebs    ) {
        this.links_root_ba_element_links = links_root_ba_element_links;
        this.links_rootnodebs = links_rootnodebs;
    }


    public List<links_Root_BA_Element_Link> getLinks_root_ba_element_links() {
        return links_root_ba_element_links;
    }

    public void addLinks_root_ba_element_link(Links_root_ba_element_link links_root_ba_element_link) {
        this.links_root_ba_element_links.add(links_root_ba_element_link);
    }
    public List<links_RootNodeB> getLinks_rootnodebs() {
        return links_rootnodebs;
    }

    public void addLinks_rootnodeb(Links_rootnodeb links_rootnodeb) {
        this.links_rootnodebs.add(links_rootnodeb);
    }

}