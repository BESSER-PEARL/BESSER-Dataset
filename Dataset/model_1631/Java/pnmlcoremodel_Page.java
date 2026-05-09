





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Page extends Node {






    private pnmlcoremodel_PetriNet pnmlcoremodel_petrinet;




    private List<pnmlcoremodel_Object> pnmlcoremodel_objects;




    private List<pnmlcoremodel_LabelProxy> pnmlcoremodel_labelproxys;




    private List<pnmlcoremodel_PageLabelProxy> pnmlcoremodel_pagelabelproxys;


    public pnmlcoremodel_Page(
    ) {
        super(
        );
        this.pnmlcoremodel_objects = new ArrayList<>();
        this.pnmlcoremodel_labelproxys = new ArrayList<>();
        this.pnmlcoremodel_pagelabelproxys = new ArrayList<>();
    }

    public pnmlcoremodel_Page(
        ArrayList<pnmlcoremodel_Object> pnmlcoremodel_objects,        ArrayList<pnmlcoremodel_LabelProxy> pnmlcoremodel_labelproxys,        ArrayList<pnmlcoremodel_PageLabelProxy> pnmlcoremodel_pagelabelproxys    ) {
        this.pnmlcoremodel_objects = pnmlcoremodel_objects;
        this.pnmlcoremodel_labelproxys = pnmlcoremodel_labelproxys;
        this.pnmlcoremodel_pagelabelproxys = pnmlcoremodel_pagelabelproxys;
    }


    public pnmlcoremodel_PetriNet getPnmlcoremodel_petrinet() {
        return pnmlcoremodel_petrinet;
    }

    public void setPnmlcoremodel_petrinet(pnmlcoremodel_PetriNet pnmlcoremodel_petrinet) {
        this.pnmlcoremodel_petrinet = pnmlcoremodel_petrinet;
    }
    public List<pnmlcoremodel_Object> getPnmlcoremodel_objects() {
        return pnmlcoremodel_objects;
    }

    public void addPnmlcoremodel_object(Pnmlcoremodel_object pnmlcoremodel_object) {
        this.pnmlcoremodel_objects.add(pnmlcoremodel_object);
    }
    public List<pnmlcoremodel_LabelProxy> getPnmlcoremodel_labelproxys() {
        return pnmlcoremodel_labelproxys;
    }

    public void addPnmlcoremodel_labelproxy(Pnmlcoremodel_labelproxy pnmlcoremodel_labelproxy) {
        this.pnmlcoremodel_labelproxys.add(pnmlcoremodel_labelproxy);
    }
    public List<pnmlcoremodel_PageLabelProxy> getPnmlcoremodel_pagelabelproxys() {
        return pnmlcoremodel_pagelabelproxys;
    }

    public void addPnmlcoremodel_pagelabelproxy(Pnmlcoremodel_pagelabelproxy pnmlcoremodel_pagelabelproxy) {
        this.pnmlcoremodel_pagelabelproxys.add(pnmlcoremodel_pagelabelproxy);
    }

}