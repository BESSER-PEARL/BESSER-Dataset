





import java.util.List;
import java.util.ArrayList;

public class avm_ValueNode  {

    private String ID;





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

    public avm_DerivedValue getAvm_derivedvalue() {
        return avm_derivedvalue;
    }

    public void setAvm_derivedvalue(avm_DerivedValue avm_derivedvalue) {
        this.avm_derivedvalue = avm_derivedvalue;
    }

}