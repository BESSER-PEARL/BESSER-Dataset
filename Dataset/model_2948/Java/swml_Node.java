





import java.util.List;
import java.util.ArrayList;

public class swml_Node  {






    private List<swml_Link> swml_links;




    private swml_Link swml_link;




    private swml_HypertextModel swml_hypertextmodel;




    private swml_Link swml_link;


    public swml_Node(
    ) {
        this.swml_links = new ArrayList<>();
    }

    public swml_Node(
        ArrayList<swml_Link> swml_links    ) {
        this.swml_links = swml_links;
    }


    public List<swml_Link> getSwml_links() {
        return swml_links;
    }

    public void addSwml_link(Swml_link swml_link) {
        this.swml_links.add(swml_link);
    }
    public swml_Link getSwml_link() {
        return swml_link;
    }

    public void setSwml_link(swml_Link swml_link) {
        this.swml_link = swml_link;
    }
    public swml_HypertextModel getSwml_hypertextmodel() {
        return swml_hypertextmodel;
    }

    public void setSwml_hypertextmodel(swml_HypertextModel swml_hypertextmodel) {
        this.swml_hypertextmodel = swml_hypertextmodel;
    }
    public swml_Link getSwml_link() {
        return swml_link;
    }

    public void setSwml_link(swml_Link swml_link) {
        this.swml_link = swml_link;
    }

}