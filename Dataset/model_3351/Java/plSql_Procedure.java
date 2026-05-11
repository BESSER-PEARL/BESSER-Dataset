





import java.util.List;
import java.util.ArrayList;

public class plSql_Procedure extends CompilationUnit, NameDeclaration {

    private String schemaName;



    public plSql_Procedure(
        String schemaName    ) {
        super(
        );
        this.schemaName = schemaName;
    }


    public String getSchemaname() {
        return schemaName;
    }

    public void setSchemaname(String schemaName) {
        this.schemaName = schemaName;
    }


}