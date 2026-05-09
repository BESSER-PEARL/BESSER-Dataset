





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Page extends Node {






    private List<pnmlcoremodel_Object> pnmlcoremodel_objects;




    private pnmlcoremodel_PetriNet pnmlcoremodel_petrinet;


    public pnmlcoremodel_Page(
    ) {
        super(
        );
        this.pnmlcoremodel_objects = new ArrayList<>();
    }

    public pnmlcoremodel_Page(
        ArrayList<pnmlcoremodel_Object> pnmlcoremodel_objects    ) {
        this.pnmlcoremodel_objects = pnmlcoremodel_objects;
    }


    public List<pnmlcoremodel_Object> getPnmlcoremodel_objects() {
        return pnmlcoremodel_objects;
    }

    public void addPnmlcoremodel_object(Pnmlcoremodel_object pnmlcoremodel_object) {
        this.pnmlcoremodel_objects.add(pnmlcoremodel_object);
    }
    public pnmlcoremodel_PetriNet getPnmlcoremodel_petrinet() {
        return pnmlcoremodel_petrinet;
    }

    public void setPnmlcoremodel_petrinet(pnmlcoremodel_PetriNet pnmlcoremodel_petrinet) {
        this.pnmlcoremodel_petrinet = pnmlcoremodel_petrinet;
    }

}