





import java.util.List;
import java.util.ArrayList;

public class ram_Classifier extends ObjectType {






    private List<ram_Operation> ram_operations;




    private ram_StructuralView ram_structuralview;




    private ram_StateView ram_stateview;


    public ram_Classifier(
    ) {
        super(
        );
        this.ram_operations = new ArrayList<>();
    }

    public ram_Classifier(
        ArrayList<ram_Operation> ram_operations    ) {
        this.ram_operations = ram_operations;
    }


    public List<ram_Operation> getRam_operations() {
        return ram_operations;
    }

    public void addRam_operation(Ram_operation ram_operation) {
        this.ram_operations.add(ram_operation);
    }
    public ram_StructuralView getRam_structuralview() {
        return ram_structuralview;
    }

    public void setRam_structuralview(ram_StructuralView ram_structuralview) {
        this.ram_structuralview = ram_structuralview;
    }
    public ram_StateView getRam_stateview() {
        return ram_stateview;
    }

    public void setRam_stateview(ram_StateView ram_stateview) {
        this.ram_stateview = ram_stateview;
    }

}