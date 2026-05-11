





import java.util.List;
import java.util.ArrayList;

public class odemcustom_TypedElement  {

    private boolean isList;





    private odemcustom_IdExpr odemcustom_idexpr;




    private odemcustom_PrimitiveType odemcustom_primitivetype;


    public odemcustom_TypedElement(
        boolean isList    ) {
        this.isList = isList;
    }


    public boolean getIslist() {
        return isList;
    }

    public void setIslist(boolean isList) {
        this.isList = isList;
    }

    public odemcustom_IdExpr getOdemcustom_idexpr() {
        return odemcustom_idexpr;
    }

    public void setOdemcustom_idexpr(odemcustom_IdExpr odemcustom_idexpr) {
        this.odemcustom_idexpr = odemcustom_idexpr;
    }
    public odemcustom_PrimitiveType getOdemcustom_primitivetype() {
        return odemcustom_primitivetype;
    }

    public void setOdemcustom_primitivetype(odemcustom_PrimitiveType odemcustom_primitivetype) {
        this.odemcustom_primitivetype = odemcustom_primitivetype;
    }

}