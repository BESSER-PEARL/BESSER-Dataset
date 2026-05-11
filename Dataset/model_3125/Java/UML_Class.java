





import java.util.List;
import java.util.ArrayList;

public class UML_Class extends Classifier {

    private String kind;





    private UML_Association uml_association;




    private List<UML_Class> uml_classs;




    private UML_Association uml_association;




    private List<UML_Association> uml_associations;




    private List<UML_Association> uml_associations;




    private UML_Class uml_class;


    public UML_Class(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml_classs = new ArrayList<>();
        this.uml_associations = new ArrayList<>();
        this.uml_associations = new ArrayList<>();
    }

    public UML_Class(
        String kind        ArrayList<UML_Class> uml_classs,        ArrayList<UML_Association> uml_associations,        ArrayList<UML_Association> uml_associations    ) {
        this.kind = kind;
        this.uml_classs = uml_classs;
        this.uml_associations = uml_associations;
        this.uml_associations = uml_associations;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public UML_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(UML_Association uml_association) {
        this.uml_association = uml_association;
    }
    public List<UML_Class> getUml_classs() {
        return uml_classs;
    }

    public void addUml_class(Uml_class uml_class) {
        this.uml_classs.add(uml_class);
    }
    public UML_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(UML_Association uml_association) {
        this.uml_association = uml_association;
    }
    public List<UML_Association> getUml_associations() {
        return uml_associations;
    }

    public void addUml_association(Uml_association uml_association) {
        this.uml_associations.add(uml_association);
    }
    public List<UML_Association> getUml_associations() {
        return uml_associations;
    }

    public void addUml_association(Uml_association uml_association) {
        this.uml_associations.add(uml_association);
    }
    public UML_Class getUml_class() {
        return uml_class;
    }

    public void setUml_class(UML_Class uml_class) {
        this.uml_class = uml_class;
    }

}