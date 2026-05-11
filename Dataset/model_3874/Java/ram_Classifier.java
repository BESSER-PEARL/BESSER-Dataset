





import java.util.List;
import java.util.ArrayList;

public class ram_Classifier extends ObjectType, Traceable {

    private boolean dataType;





    private List<ram_Operation> ram_operations;




    private ram_StateView ram_stateview;




    private ram_StructuralView ram_structuralview;




    private List<ram_Classifier> ram_classifiers;


    public ram_Classifier(
        boolean dataType    ) {
        super(
        );
        this.dataType = dataType;
        this.ram_operations = new ArrayList<>();
        this.ram_classifiers = new ArrayList<>();
    }

    public ram_Classifier(
        boolean dataType        ArrayList<ram_Operation> ram_operations,        ArrayList<ram_Classifier> ram_classifiers    ) {
        this.dataType = dataType;
        this.ram_operations = ram_operations;
        this.ram_classifiers = ram_classifiers;
    }

    public boolean getDatatype() {
        return dataType;
    }

    public void setDatatype(boolean dataType) {
        this.dataType = dataType;
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
    public ram_StructuralView getRam_structuralview() {
        return ram_structuralview;
    }

    public void setRam_structuralview(ram_StructuralView ram_structuralview) {
        this.ram_structuralview = ram_structuralview;
    }
    public List<ram_Classifier> getRam_classifiers() {
        return ram_classifiers;
    }

    public void addRam_classifier(Ram_classifier ram_classifier) {
        this.ram_classifiers.add(ram_classifier);
    }

}