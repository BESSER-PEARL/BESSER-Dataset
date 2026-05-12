





import java.util.List;
import java.util.ArrayList;

public class nupn_SizeType  {

    private String places;
    private String arcs;
    private String transitions;



    public nupn_SizeType(
        String places,        String arcs,        String transitions    ) {
        this.places = places;
        this.arcs = arcs;
        this.transitions = transitions;
    }


    public String getPlaces() {
        return places;
    }

    public void setPlaces(String places) {
        this.places = places;
    }
    public String getArcs() {
        return arcs;
    }

    public void setArcs(String arcs) {
        this.arcs = arcs;
    }
    public String getTransitions() {
        return transitions;
    }

    public void setTransitions(String transitions) {
        this.transitions = transitions;
    }


}