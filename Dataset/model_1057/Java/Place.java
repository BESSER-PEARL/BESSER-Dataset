





import java.util.List;
import java.util.ArrayList;

public class Place  {






    private PetriNet_PlaceToTransArc petrinet_placetotransarc;




    private PetriNet_PetriNet petrinet_petrinet;


    public Place(
    ) {
    }



    public PetriNet_PlaceToTransArc getPetrinet_placetotransarc() {
        return petrinet_placetotransarc;
    }

    public void setPetrinet_placetotransarc(PetriNet_PlaceToTransArc petrinet_placetotransarc) {
        this.petrinet_placetotransarc = petrinet_placetotransarc;
    }
    public PetriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(PetriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}