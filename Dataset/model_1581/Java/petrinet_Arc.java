





import java.util.List;
import java.util.ArrayList;

public class petrinet_Arc  {

    private String name;
    private int weight;
    private String arcType;





    private petrinet_Noeud petrinet_noeud;




    private petrinet_PetriNet petrinet_petrinet;




    private petrinet_Noeud petrinet_noeud;


    public petrinet_Arc(
        String name,        int weight,        String arcType    ) {
        this.name = name;
        this.weight = weight;
        this.arcType = arcType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public String getArctype() {
        return arcType;
    }

    public void setArctype(String arcType) {
        this.arcType = arcType;
    }

    public petrinet_Noeud getPetrinet_noeud() {
        return petrinet_noeud;
    }

    public void setPetrinet_noeud(petrinet_Noeud petrinet_noeud) {
        this.petrinet_noeud = petrinet_noeud;
    }
    public petrinet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }
    public petrinet_Noeud getPetrinet_noeud() {
        return petrinet_noeud;
    }

    public void setPetrinet_noeud(petrinet_Noeud petrinet_noeud) {
        this.petrinet_noeud = petrinet_noeud;
    }

}