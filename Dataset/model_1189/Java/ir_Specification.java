





import java.util.List;
import java.util.ArrayList;

public class ir_Specification  {






    private List<ir_EFPrimitiveType> ir_efprimitivetypes;




    private List<ir_EFTupleType> ir_eftupletypes;




    private List<ir_Operation> ir_operations;


    public ir_Specification(
    ) {
        this.ir_efprimitivetypes = new ArrayList<>();
        this.ir_eftupletypes = new ArrayList<>();
        this.ir_operations = new ArrayList<>();
    }

    public ir_Specification(
        ArrayList<ir_EFPrimitiveType> ir_efprimitivetypes,        ArrayList<ir_EFTupleType> ir_eftupletypes,        ArrayList<ir_Operation> ir_operations    ) {
        this.ir_efprimitivetypes = ir_efprimitivetypes;
        this.ir_eftupletypes = ir_eftupletypes;
        this.ir_operations = ir_operations;
    }


    public List<ir_EFPrimitiveType> getIr_efprimitivetypes() {
        return ir_efprimitivetypes;
    }

    public void addIr_efprimitivetype(Ir_efprimitivetype ir_efprimitivetype) {
        this.ir_efprimitivetypes.add(ir_efprimitivetype);
    }
    public List<ir_EFTupleType> getIr_eftupletypes() {
        return ir_eftupletypes;
    }

    public void addIr_eftupletype(Ir_eftupletype ir_eftupletype) {
        this.ir_eftupletypes.add(ir_eftupletype);
    }
    public List<ir_Operation> getIr_operations() {
        return ir_operations;
    }

    public void addIr_operation(Ir_operation ir_operation) {
        this.ir_operations.add(ir_operation);
    }

}