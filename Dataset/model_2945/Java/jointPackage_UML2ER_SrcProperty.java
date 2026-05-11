





import java.util.List;
import java.util.ArrayList;

public class jointPackage_UML2ER_SrcProperty extends SrcNamedElement {

    private boolean isContainment;
    private String primitiveType;



    public jointPackage_UML2ER_SrcProperty(
        boolean isContainment,        String primitiveType    ) {
        super(
        );
        this.isContainment = isContainment;
        this.primitiveType = primitiveType;
    }


    public boolean getIscontainment() {
        return isContainment;
    }

    public void setIscontainment(boolean isContainment) {
        this.isContainment = isContainment;
    }
    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }


}