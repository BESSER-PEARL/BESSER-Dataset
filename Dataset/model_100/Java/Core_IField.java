





import java.util.List;
import java.util.ArrayList;

public class Core_IField extends IMember {

    private String isEnumConstant;
    private String constant;
    private String typeSignature;
    private String isVolatile;
    private String isTransient;



    public Core_IField(
        String isEnumConstant,        String constant,        String typeSignature,        String isVolatile,        String isTransient    ) {
        super(
        );
        this.isEnumConstant = isEnumConstant;
        this.constant = constant;
        this.typeSignature = typeSignature;
        this.isVolatile = isVolatile;
        this.isTransient = isTransient;
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
    public String getIstransient() {
        return isTransient;
    }

    public void setIstransient(String isTransient) {
        this.isTransient = isTransient;
    }


}