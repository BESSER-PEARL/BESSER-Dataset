





import java.util.List;
import java.util.ArrayList;

public class dsl_Type  {

    private String primType;





    private dsl_FieldDeclaration dsl_fielddeclaration;


    public dsl_Type(
        String primType    ) {
        this.primType = primType;
    }


    public String getPrimtype() {
        return primType;
    }

    public void setPrimtype(String primType) {
        this.primType = primType;
    }

    public dsl_FieldDeclaration getDsl_fielddeclaration() {
        return dsl_fielddeclaration;
    }

    public void setDsl_fielddeclaration(dsl_FieldDeclaration dsl_fielddeclaration) {
        this.dsl_fielddeclaration = dsl_fielddeclaration;
    }

}