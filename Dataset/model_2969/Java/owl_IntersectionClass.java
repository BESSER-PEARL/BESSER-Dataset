





import java.util.List;
import java.util.ArrayList;

public class owl_IntersectionClass extends OWLClass {






    private owl_OWLClass owl_owlclass;




    private List<owl_OWLClass> owl_owlclasss;


    public owl_IntersectionClass(
    ) {
        super(
        );
        this.owl_owlclasss = new ArrayList<>();
    }

    public owl_IntersectionClass(
        ArrayList<owl_OWLClass> owl_owlclasss    ) {
        this.owl_owlclasss = owl_owlclasss;
    }


    public owl_OWLClass getOwl_owlclass() {
        return owl_owlclass;
    }

    public void setOwl_owlclass(owl_OWLClass owl_owlclass) {
        this.owl_owlclass = owl_owlclass;
    }
    public List<owl_OWLClass> getOwl_owlclasss() {
        return owl_owlclasss;
    }

    public void addOwl_owlclass(Owl_owlclass owl_owlclass) {
        this.owl_owlclasss.add(owl_owlclass);
    }

}