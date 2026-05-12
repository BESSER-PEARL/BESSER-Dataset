





import java.util.List;
import java.util.ArrayList;

public class plSql_Function extends CompilationUnit, NameDeclaration {

    private String schemaName;
    private String returnType;



    public plSql_Function(
        String schemaName,        String returnType    ) {
        super(
        );
        this.schemaName = schemaName;
        this.returnType = returnType;
    }


    public String getSchemaname() {
        return schemaName;
    }

    public void setSchemaname(String schemaName) {
        this.schemaName = schemaName;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }


}