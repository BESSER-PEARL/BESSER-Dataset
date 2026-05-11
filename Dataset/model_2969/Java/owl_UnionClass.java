





import java.util.List;
import java.util.ArrayList;

public class owl_UnionClass extends OWLClass {






    private List<owl_OWLClass> owl_owlclasss;




    private owl_OWLClass owl_owlclass;


    public owl_UnionClass(
    ) {
        super(
        );
        this.owl_owlclasss = new ArrayList<>();
    }

    public owl_UnionClass(
        ArrayList<owl_OWLClass> owl_owlclasss    ) {
        this.owl_owlclasss = owl_owlclasss;
    }


    public List<owl_OWLClass> getOwl_owlclasss() {
        return owl_owlclasss;
    }

    public void addOwl_owlclass(Owl_owlclass owl_owlclass) {
        this.owl_owlclasss.add(owl_owlclass);
    }
    public owl_OWLClass getOwl_owlclass() {
        return owl_owlclass;
    }

    public void setOwl_owlclass(owl_OWLClass owl_owlclass) {
        this.owl_owlclass = owl_owlclass;
    }

}