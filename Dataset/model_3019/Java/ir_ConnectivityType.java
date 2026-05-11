





import java.util.List;
import java.util.ArrayList;

public class ir_ConnectivityType extends IrType {






    private ir_ConnectivityVariable ir_connectivityvariable;




    private List<ir_Connectivity> ir_connectivitys;




    private ir_BaseType ir_basetype;


    public ir_ConnectivityType(
    ) {
        super(
        );
        this.ir_connectivitys = new ArrayList<>();
    }

    public ir_ConnectivityType(
        ArrayList<ir_Connectivity> ir_connectivitys    ) {
        this.ir_connectivitys = ir_connectivitys;
    }


    public ir_ConnectivityVariable getIr_connectivityvariable() {
        return ir_connectivityvariable;
    }

    public void setIr_connectivityvariable(ir_ConnectivityVariable ir_connectivityvariable) {
        this.ir_connectivityvariable = ir_connectivityvariable;
    }
    public List<ir_Connectivity> getIr_connectivitys() {
        return ir_connectivitys;
    }

    public void addIr_connectivity(Ir_connectivity ir_connectivity) {
        this.ir_connectivitys.add(ir_connectivity);
    }
    public ir_BaseType getIr_basetype() {
        return ir_basetype;
    }

    public void setIr_basetype(ir_BaseType ir_basetype) {
        this.ir_basetype = ir_basetype;
    }

}