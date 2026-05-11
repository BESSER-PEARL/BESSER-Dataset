





import java.util.List;
import java.util.ArrayList;

public class aS3_VariableDeclaration extends Statement, forInClauseDecl {

    private String name;
    private String anytype;





    private aS3_EObject as3_eobject;


    public aS3_VariableDeclaration(
        String name,        String anytype    ) {
        super(
        );
        this.name = name;
        this.anytype = anytype;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAnytype() {
        return anytype;
    }

    public void setAnytype(String anytype) {
        this.anytype = anytype;
    }

    public aS3_EObject getAs3_eobject() {
        return as3_eobject;
    }

    public void setAs3_eobject(aS3_EObject as3_eobject) {
        this.as3_eobject = as3_eobject;
    }

}