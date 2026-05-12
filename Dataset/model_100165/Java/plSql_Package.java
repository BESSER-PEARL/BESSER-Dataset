





import java.util.List;
import java.util.ArrayList;

public class plSql_Package extends CompilationUnit, NameDeclaration {

    private String schemaName;
    private String endName;



    public plSql_Package(
        String schemaName,        String endName    ) {
        super(
        );
        this.schemaName = schemaName;
        this.endName = endName;
    }


    public String getSchemaname() {
        return schemaName;
    }

    public void setSchemaname(String schemaName) {
        this.schemaName = schemaName;
    }
    public String getEndname() {
        return endName;
    }

    public void setEndname(String endName) {
        this.endName = endName;
    }


}