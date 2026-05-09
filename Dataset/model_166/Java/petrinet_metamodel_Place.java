





import java.util.List;
import java.util.ArrayList;

public class petrinet_metamodel_Place extends Element {

    private int radius;
    private String fill_colour;
    private int coordinates;





    private petrinet_metamodel_PetriNet petrinet_metamodel_petrinet;




    private List<petrinet_metamodel_TransToPlaceArc> petrinet_metamodel_transtoplacearcs;




    private petrinet_metamodel_PetriNet petrinet_metamodel_petrinet;




    private List<petrinet_metamodel_PlaceToTransArc> petrinet_metamodel_placetotransarcs;




    private petrinet_metamodel_TransToPlaceArc petrinet_metamodel_transtoplacearc;




    private petrinet_metamodel_PlaceToTransArc petrinet_metamodel_placetotransarc;


    public petrinet_metamodel_Place(
        int radius,        String fill_colour,        int coordinates    ) {
        super(
        );
        this.radius = radius;
        this.fill_colour = fill_colour;
        this.coordinates = coordinates;
        this.petrinet_metamodel_transtoplacearcs = new ArrayList<>();
        this.petrinet_metamodel_placetotransarcs = new ArrayList<>();
    }

    public petrinet_metamodel_Place(
        int radius,        String fill_colour,        int coordinates        ArrayList<petrinet_metamodel_TransToPlaceArc> petrinet_metamodel_transtoplacearcs,        ArrayList<petrinet_metamodel_PlaceToTransArc> petrinet_metamodel_placetotransarcs    ) {
        this.radius = radius;
        this.fill_colour = fill_colour;
        this.coordinates = coordinates;
        this.petrinet_metamodel_transtoplacearcs = petrinet_metamodel_transtoplacearcs;
        this.petrinet_metamodel_placetotransarcs = petrinet_metamodel_placetotransarcs;
    }

    public int getRadius() {
        return radius;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }
    public String getFill_colour() {
        return fill_colour;
    }

    public void setFill_colour(String fill_colour) {
        this.fill_colour = fill_colour;
    }
    public int getCoordinates() {
        return coordinates;
    }

    public void setCoordinates(int coordinates) {
        this.coordinates = coordinates;
    }

    public petrinet_metamodel_PetriNet getPetrinet_metamodel_petrinet() {
        return petrinet_metamodel_petrinet;
    }

    public void setPetrinet_metamodel_petrinet(petrinet_metamodel_PetriNet petrinet_metamodel_petrinet) {
        this.petrinet_metamodel_petrinet = petrinet_metamodel_petrinet;
    }
    public List<petrinet_metamodel_TransToPlaceArc> getPetrinet_metamodel_transtoplacearcs() {
        return petrinet_metamodel_transtoplacearcs;
    }

    public void addPetrinet_metamodel_transtoplacearc(Petrinet_metamodel_transtoplacearc petrinet_metamodel_transtoplacearc) {
        this.petrinet_metamodel_transtoplacearcs.add(petrinet_metamodel_transtoplacearc);
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

}