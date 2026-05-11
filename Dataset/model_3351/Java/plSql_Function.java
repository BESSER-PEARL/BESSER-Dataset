





import java.util.List;
import java.util.ArrayList;

public class plSql_Function extends CompilationUnit, NameDeclaration {

    private String returnType;
    private String schemaName;



    public plSql_Function(
        String returnType,        String schemaName    ) {
        super(
        );
        this.returnType = returnType;
        this.schemaName = schemaName;
    }


    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getSchemaname() {
        return schemaName;
    }

    public void setSchemaname(String schemaName) {
        this.schemaName = schemaName;
    }


}