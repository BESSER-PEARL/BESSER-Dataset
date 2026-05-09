





import java.util.List;
import java.util.ArrayList;

public class Core_IField extends IMember {

    private String typeSignature;
    private String isTransient;
    private String isVolatile;
    private String isEnumConstant;
    private String constant;



    public Core_IField(
        String typeSignature,        String isTransient,        String isVolatile,        String isEnumConstant,        String constant    ) {
        super(
        );
        this.typeSignature = typeSignature;
        this.isTransient = isTransient;
        this.isVolatile = isVolatile;
        this.isEnumConstant = isEnumConstant;
        this.constant = constant;
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
    public String getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(String isVolatile) {
        this.isVolatile = isVolatile;
    }
    public String getIsenumconstant() {
        return isEnumConstant;
    }

    public void setIsenumconstant(String isEnumConstant) {
        this.isEnumConstant = isEnumConstant;
    }
    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }


}