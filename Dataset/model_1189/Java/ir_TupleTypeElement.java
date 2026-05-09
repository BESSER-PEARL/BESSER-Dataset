





import java.util.List;
import java.util.ArrayList;

public class ir_TupleTypeElement  {

    private String name;





    private ir_EFTupleType ir_eftupletype;




    private ir_TypeRef ir_typeref;


    public ir_TupleTypeElement(
        String name    ) {
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
    public ir_TypeRef getIr_typeref() {
        return ir_typeref;
    }

    public void setIr_typeref(ir_TypeRef ir_typeref) {
        this.ir_typeref = ir_typeref;
    }

}