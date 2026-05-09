





import java.util.List;
import java.util.ArrayList;

public class petrinet_Reseau  {

    private String nom;





    private List<petrinet_Arc> petrinet_arcs;




    private List<petrinet_Element> petrinet_elements;


    public petrinet_Reseau(
        String nom    ) {
        this.nom = nom;
        this.petrinet_arcs = new ArrayList<>();
        this.petrinet_elements = new ArrayList<>();
    }

    public petrinet_Reseau(
        String nom        ArrayList<petrinet_Arc> petrinet_arcs,        ArrayList<petrinet_Element> petrinet_elements    ) {
        this.nom = nom;
        this.petrinet_arcs = petrinet_arcs;
        this.petrinet_elements = petrinet_elements;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<petrinet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public List<petrinet_Element> getPetrinet_elements() {
        return petrinet_elements;
    }

    public void addPetrinet_element(Petrinet_element petrinet_element) {
        this.petrinet_elements.add(petrinet_element);
    }

}