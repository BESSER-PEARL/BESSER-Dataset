





import java.util.List;
import java.util.ArrayList;

public class petrinet_metamodel_Transition extends Element {






    private petrinet_metamodel_Rectangle petrinet_metamodel_rectangle;




    private petrinet_metamodel_PetriNet petrinet_metamodel_petrinet;




    private petrinet_metamodel_PetriNet petrinet_metamodel_petrinet;




    private List<petrinet_metamodel_PlaceToTransArc> petrinet_metamodel_placetotransarcs;




    private petrinet_metamodel_TransToPlaceArc petrinet_metamodel_transtoplacearc;




    private petrinet_metamodel_PlaceToTransArc petrinet_metamodel_placetotransarc;




    private petrinet_metamodel_Rectangle petrinet_metamodel_rectangle;




    private List<petrinet_metamodel_TransToPlaceArc> petrinet_metamodel_transtoplacearcs;


    public petrinet_metamodel_Transition(
    ) {
        super(
        );
        this.petrinet_metamodel_placetotransarcs = new ArrayList<>();
        this.petrinet_metamodel_transtoplacearcs = new ArrayList<>();
    }

    public petrinet_metamodel_Transition(
        ArrayList<petrinet_metamodel_PlaceToTransArc> petrinet_metamodel_placetotransarcs,        ArrayList<petrinet_metamodel_TransToPlaceArc> petrinet_metamodel_transtoplacearcs    ) {
        this.petrinet_metamodel_placetotransarcs = petrinet_metamodel_placetotransarcs;
        this.petrinet_metamodel_transtoplacearcs = petrinet_metamodel_transtoplacearcs;
    }


    public petrinet_metamodel_Rectangle getPetrinet_metamodel_rectangle() {
        return petrinet_metamodel_rectangle;
    }

    public void setPetrinet_metamodel_rectangle(petrinet_metamodel_Rectangle petrinet_metamodel_rectangle) {
        this.petrinet_metamodel_rectangle = petrinet_metamodel_rectangle;
    }
    public petrinet_metamodel_PetriNet getPetrinet_metamodel_petrinet() {
        return petrinet_metamodel_petrinet;
    }

    public void setPetrinet_metamodel_petrinet(petrinet_metamodel_PetriNet petrinet_metamodel_petrinet) {
        this.petrinet_metamodel_petrinet = petrinet_metamodel_petrinet;
    }
    public petrinet_metamodel_PetriNet getPetrinet_metamodel_petrinet() {
        return petrinet_metamodel_petrinet;
    }

    public void setPetrinet_metamodel_petrinet(petrinet_metamodel_PetriNet petrinet_metamodel_petrinet) {
        this.petrinet_metamodel_petrinet = petrinet_metamodel_petrinet;
    }
    public List<petrinet_metamodel_PlaceToTransArc> getPetrinet_metamodel_placetotransarcs() {
        return petrinet_metamodel_placetotransarcs;
    }

    public void addPetrinet_metamodel_placetotransarc(Petrinet_metamodel_placetotransarc petrinet_metamodel_placetotransarc) {
        this.petrinet_metamodel_placetotransarcs.add(petrinet_metamodel_placetotransarc);
    }
    public petrinet_metamodel_TransToPlaceArc getPetrinet_metamodel_transtoplacearc() {
        return petrinet_metamodel_transtoplacearc;
    }

    public void setPetrinet_metamodel_transtoplacearc(petrinet_metamodel_TransToPlaceArc petrinet_metamodel_transtoplacearc) {
        this.petrinet_metamodel_transtoplacearc = petrinet_metamodel_transtoplacearc;
    }
    public petrinet_metamodel_PlaceToTransArc getPetrinet_metamodel_placetotransarc() {
        return petrinet_metamodel_placetotransarc;
    }

    public void setPetrinet_metamodel_placetotransarc(petrinet_metamodel_PlaceToTransArc petrinet_metamodel_placetotransarc) {
        this.petrinet_metamodel_placetotransarc = petrinet_metamodel_placetotransarc;
    }
    public petrinet_metamodel_Rectangle getPetrinet_metamodel_rectangle() {
        return petrinet_metamodel_rectangle;
    }

    public void setPetrinet_metamodel_rectangle(petrinet_metamodel_Rectangle petrinet_metamodel_rectangle) {
        this.petrinet_metamodel_rectangle = petrinet_metamodel_rectangle;
    }
    public List<petrinet_metamodel_TransToPlaceArc> getPetrinet_metamodel_transtoplacearcs() {
        return petrinet_metamodel_transtoplacearcs;
    }

    public void addPetrinet_metamodel_transtoplacearc(Petrinet_metamodel_transtoplacearc petrinet_metamodel_transtoplacearc) {
        this.petrinet_metamodel_transtoplacearcs.add(petrinet_metamodel_transtoplacearc);
    }

}