





import java.util.List;
import java.util.ArrayList;

public class ram_Classifier extends ObjectType {






    private List<ram_AssociationEnd> ram_associationends;




    private ram_Class ram_class;




    private ram_AssociationEnd ram_associationend;




    private ram_StructuralView ram_structuralview;




    private List<ram_Operation> ram_operations;




    private ram_StateView ram_stateview;


    public ram_Classifier(
    ) {
        super(
        );
        this.ram_associationends = new ArrayList<>();
        this.ram_operations = new ArrayList<>();
    }

    public ram_Classifier(
        ArrayList<ram_AssociationEnd> ram_associationends,        ArrayList<ram_Operation> ram_operations    ) {
        this.ram_associationends = ram_associationends;
        this.ram_operations = ram_operations;
    }


    public List<ram_AssociationEnd> getRam_associationends() {
        return ram_associationends;
    }

    public void addRam_associationend(Ram_associationend ram_associationend) {
        this.ram_associationends.add(ram_associationend);
    }
    public ram_Class getRam_class() {
        return ram_class;
    }

    public void setRam_class(ram_Class ram_class) {
        this.ram_class = ram_class;
    }
    public ram_AssociationEnd getRam_associationend() {
        return ram_associationend;
    }

    public void setRam_associationend(ram_AssociationEnd ram_associationend) {
        this.ram_associationend = ram_associationend;
    }
    public ram_StructuralView getRam_structuralview() {
        return ram_structuralview;
    }

    public void setRam_structuralview(ram_StructuralView ram_structuralview) {
        this.ram_structuralview = ram_structuralview;
    }
    public List<ram_Operation> getRam_operations() {
        return ram_operations;
    }

    public void addRam_operation(Ram_operation ram_operation) {
        this.ram_operations.add(ram_operation);
    }
    public ram_StateView getRam_stateview() {
        return ram_stateview;
    }

    public void setRam_stateview(ram_StateView ram_stateview) {
        this.ram_stateview = ram_stateview;
    }

}