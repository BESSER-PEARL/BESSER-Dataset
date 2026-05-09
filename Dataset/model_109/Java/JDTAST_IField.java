





import java.util.List;
import java.util.ArrayList;

public class JDTAST_IField extends IMember {

    private String typeSignature;
    private String isEnumConstant;
    private String constant;
    private String isTransient;
    private String isVolatile;





    private JDTAST_IType jdtast_itype;


    public JDTAST_IField(
        String typeSignature,        String isEnumConstant,        String constant,        String isTransient,        String isVolatile    ) {
        super(
        );
        this.typeSignature = typeSignature;
        this.isEnumConstant = isEnumConstant;
        this.constant = constant;
        this.isTransient = isTransient;
        this.isVolatile = isVolatile;
    }


    public String getTypesignature() {
        return typeSignature;
    }

    public void setTypesignature(String typeSignature) {
        this.typeSignature = typeSignature;
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

    public JDTAST_IType getJdtast_itype() {
        return jdtast_itype;
    }

    public void setJdtast_itype(JDTAST_IType jdtast_itype) {
        this.jdtast_itype = jdtast_itype;
    }

}