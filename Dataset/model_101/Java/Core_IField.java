





import java.util.List;
import java.util.ArrayList;

public class Core_IField extends IMember {

    private String isTransient;
    private String isEnumConstant;
    private String constant;
    private String isVolatile;
    private String typeSignature;



    public Core_IField(
        String isTransient,        String isEnumConstant,        String constant,        String isVolatile,        String typeSignature    ) {
        super(
        );
        this.isTransient = isTransient;
        this.isEnumConstant = isEnumConstant;
        this.constant = constant;
        this.isVolatile = isVolatile;
        this.typeSignature = typeSignature;
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
    public String getTypesignature() {
        return typeSignature;
    }

    public void setTypesignature(String typeSignature) {
        this.typeSignature = typeSignature;
    }


}