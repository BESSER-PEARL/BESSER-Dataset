





import java.util.List;
import java.util.ArrayList;

public class Core_Parameter  {

    private String type;
    private String name;





    private PrimitiveTypes_Core_IMethod primitivetypes_core_imethod;


    public Core_Parameter(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PrimitiveTypes_Core_IMethod getPrimitivetypes_core_imethod() {
        return primitivetypes_core_imethod;
    }

    public void setPrimitivetypes_core_imethod(PrimitiveTypes_Core_IMethod primitivetypes_core_imethod) {
        this.primitivetypes_core_imethod = primitivetypes_core_imethod;
    }

}