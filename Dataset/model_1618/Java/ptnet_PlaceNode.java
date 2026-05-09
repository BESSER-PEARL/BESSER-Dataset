





import java.util.List;
import java.util.ArrayList;

public class ptnet_PlaceNode extends Node {






    private List<ptnet_RefPlace> ptnet_refplaces;




    private ptnet_RefPlace ptnet_refplace;


    public ptnet_PlaceNode(
    ) {
        super(
        );
        this.ptnet_refplaces = new ArrayList<>();
    }

    public ptnet_PlaceNode(
        ArrayList<ptnet_RefPlace> ptnet_refplaces    ) {
        this.ptnet_refplaces = ptnet_refplaces;
    }


    public List<ptnet_RefPlace> getPtnet_refplaces() {
        return ptnet_refplaces;
    }

    public void addPtnet_refplace(Ptnet_refplace ptnet_refplace) {
        this.ptnet_refplaces.add(ptnet_refplace);
    }
    public ptnet_RefPlace getPtnet_refplace() {
        return ptnet_refplace;
    }

    public void setPtnet_refplace(ptnet_RefPlace ptnet_refplace) {
        this.ptnet_refplace = ptnet_refplace;
    }

}