





import java.util.List;
import java.util.ArrayList;

public class links_Root_BA_Element_Link  {

    private String name;





    private links_RootNodeB links_rootnodeb;


    public links_Root_BA_Element_Link(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public links_RootNodeB getLinks_rootnodeb() {
        return links_rootnodeb;
    }

    public void setLinks_rootnodeb(links_RootNodeB links_rootnodeb) {
        this.links_rootnodeb = links_rootnodeb;
    }

}