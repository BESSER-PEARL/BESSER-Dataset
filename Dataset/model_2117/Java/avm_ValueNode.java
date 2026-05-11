





import java.util.List;
import java.util.ArrayList;

public class avm_ValueNode  {

    private String ID;





    private avm_ValueFlowMux avm_valueflowmux;




    private avm_DerivedValue avm_derivedvalue;


    public avm_ValueNode(
        String ID    ) {
        this.ID = ID;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public avm_ValueFlowMux getAvm_valueflowmux() {
        return avm_valueflowmux;
    }

    public void setAvm_valueflowmux(avm_ValueFlowMux avm_valueflowmux) {
        this.avm_valueflowmux = avm_valueflowmux;
    }
    public avm_DerivedValue getAvm_derivedvalue() {
        return avm_derivedvalue;
    }

    public void setAvm_derivedvalue(avm_DerivedValue avm_derivedvalue) {
        this.avm_derivedvalue = avm_derivedvalue;
    }

}