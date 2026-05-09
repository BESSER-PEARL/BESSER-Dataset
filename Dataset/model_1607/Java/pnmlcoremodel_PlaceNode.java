





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_PlaceNode extends Node {






    private List<pnmlcoremodel_RefPlace> pnmlcoremodel_refplaces;




    private pnmlcoremodel_RefPlace pnmlcoremodel_refplace;


    public pnmlcoremodel_PlaceNode(
    ) {
        super(
        );
        this.pnmlcoremodel_refplaces = new ArrayList<>();
    }

    public pnmlcoremodel_PlaceNode(
        ArrayList<pnmlcoremodel_RefPlace> pnmlcoremodel_refplaces    ) {
        this.pnmlcoremodel_refplaces = pnmlcoremodel_refplaces;
    }


    public List<pnmlcoremodel_RefPlace> getPnmlcoremodel_refplaces() {
        return pnmlcoremodel_refplaces;
    }

    public void addPnmlcoremodel_refplace(Pnmlcoremodel_refplace pnmlcoremodel_refplace) {
        this.pnmlcoremodel_refplaces.add(pnmlcoremodel_refplace);
    }
    public pnmlcoremodel_RefPlace getPnmlcoremodel_refplace() {
        return pnmlcoremodel_refplace;
    }

    public void setPnmlcoremodel_refplace(pnmlcoremodel_RefPlace pnmlcoremodel_refplace) {
        this.pnmlcoremodel_refplace = pnmlcoremodel_refplace;
    }

}