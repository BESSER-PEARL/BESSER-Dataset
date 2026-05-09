





import java.util.List;
import java.util.ArrayList;

public class Core_IClassFile extends ITypeRoot {

    private String isClass;
    private String isInterface;





    private PrimitiveTypes_Core_IPackageFragment primitivetypes_core_ipackagefragment;


    public Core_IClassFile(
        String isClass,        String isInterface    ) {
        super(
        );
        this.isClass = isClass;
        this.isInterface = isInterface;
    }


    public String getIsclass() {
        return isClass;
    }

    public void setIsclass(String isClass) {
        this.isClass = isClass;
    }
    public String getIsinterface() {
        return isInterface;
    }

    public void setIsinterface(String isInterface) {
        this.isInterface = isInterface;
    }

    public PrimitiveTypes_Core_IPackageFragment getPrimitivetypes_core_ipackagefragment() {
        return primitivetypes_core_ipackagefragment;
    }

    public void setPrimitivetypes_core_ipackagefragment(PrimitiveTypes_Core_IPackageFragment primitivetypes_core_ipackagefragment) {
        this.primitivetypes_core_ipackagefragment = primitivetypes_core_ipackagefragment;
    }

}