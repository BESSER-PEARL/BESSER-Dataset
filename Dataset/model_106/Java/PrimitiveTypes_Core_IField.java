





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_IField extends IMember {

    private String isEnumConstant;
    private String typeSignature;
    private String isTransient;
    private String constant;
    private String isVolatile;



    public PrimitiveTypes_Core_IField(
        String isEnumConstant,        String typeSignature,        String isTransient,        String constant,        String isVolatile    ) {
        super(
        );
        this.isEnumConstant = isEnumConstant;
        this.typeSignature = typeSignature;
        this.isTransient = isTransient;
        this.constant = constant;
        this.isVolatile = isVolatile;
    }


    public String getIsenumconstant() {
        return isEnumConstant;
    }

    public void setIsenumconstant(String isEnumConstant) {
        this.isEnumConstant = isEnumConstant;
    }
    public String getTypesignature() {
        return typeSignature;
    }

    public void setTypesignature(String typeSignature) {
        this.typeSignature = typeSignature;
    }
    public String getIstransient() {
        return isTransient;
    }

    public void setIstransient(String isTransient) {
        this.isTransient = isTransient;
    }
    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }
    public String getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(String isVolatile) {
        this.isVolatile = isVolatile;
    }


}