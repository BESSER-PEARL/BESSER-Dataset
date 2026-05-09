





import java.util.List;
import java.util.ArrayList;

public class ir_TupleFieldRef extends PropertyFeatureRef {

    private String name;





    private ir_EFTupleType ir_eftupletype;


    public ir_TupleFieldRef(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_EFTupleType getIr_eftupletype() {
        return ir_eftupletype;
    }

    public void setIr_eftupletype(ir_EFTupleType ir_eftupletype) {
        this.ir_eftupletype = ir_eftupletype;
    }

}