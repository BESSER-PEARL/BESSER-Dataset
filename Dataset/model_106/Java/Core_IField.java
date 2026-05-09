





import java.util.List;
import java.util.ArrayList;

public class Core_IField extends IMember {

    private String constant;
    private String isTransient;
    private String isEnumConstant;
    private String typeSignature;
    private String isVolatile;



    public Core_IField(
        String constant,        String isTransient,        String isEnumConstant,        String typeSignature,        String isVolatile    ) {
        super(
        );
        this.constant = constant;
        this.isTransient = isTransient;
        this.isEnumConstant = isEnumConstant;
        this.typeSignature = typeSignature;
        this.isVolatile = isVolatile;
    }


    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }
    public String getIstransient() {
        return isTransient;
    }

    public void setIstransient(String isTransient) {
        this.isTransient = isTransient;
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
    public String getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(String isVolatile) {
        this.isVolatile = isVolatile;
    }


}