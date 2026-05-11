





import java.util.List;
import java.util.ArrayList;

public class uml_UMLSpecification extends NamedElement {






    private List<uml_Association> uml_associations;




    private List<uml_Class> uml_classs;


    public uml_UMLSpecification(
    ) {
        super(
        );
        this.uml_associations = new ArrayList<>();
        this.uml_classs = new ArrayList<>();
    }

    public uml_UMLSpecification(
        ArrayList<uml_Association> uml_associations,        ArrayList<uml_Class> uml_classs    ) {
        this.uml_associations = uml_associations;
        this.uml_classs = uml_classs;
    }


    public List<uml_Association> getUml_associations() {
        return uml_associations;
    }

    public void addUml_association(Uml_association uml_association) {
        this.uml_associations.add(uml_association);
    }
    public List<uml_Class> getUml_classs() {
        return uml_classs;
    }

    public void addUml_class(Uml_class uml_class) {
        this.uml_classs.add(uml_class);
    }

}