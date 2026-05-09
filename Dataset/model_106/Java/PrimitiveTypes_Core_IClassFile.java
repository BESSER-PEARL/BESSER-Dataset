





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_IClassFile extends ITypeRoot {

    private String isInterface;
    private String isClass;





    private Core_IType core_itype;


    public PrimitiveTypes_Core_IClassFile(
        String isInterface,        String isClass    ) {
        super(
        );
        this.isInterface = isInterface;
        this.isClass = isClass;
    }


    public String getIsinterface() {
        return isInterface;
    }

    public void setIsinterface(String isInterface) {
        this.isInterface = isInterface;
    }
    public String getIsclass() {
        return isClass;
    }

    public void setIsclass(String isClass) {
        this.isClass = isClass;
    }

    public Core_IType getCore_itype() {
        return core_itype;
    }

    public void setCore_itype(Core_IType core_itype) {
        this.core_itype = core_itype;
    }

}