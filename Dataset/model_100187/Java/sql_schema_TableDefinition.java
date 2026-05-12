





import java.util.List;
import java.util.ArrayList;

public class sql_schema_TableDefinition extends schema_SQLSchemaDefinitionStatement, EObject {

    private String label;
    private String scope;





    private SchemaQualifiedName schemaqualifiedname;


    public sql_schema_TableDefinition(
        String label,        String scope    ) {
        super(
        );
        this.label = label;
        this.scope = scope;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }

    public SchemaQualifiedName getSchemaqualifiedname() {
        return schemaqualifiedname;
    }

    public void setSchemaqualifiedname(SchemaQualifiedName schemaqualifiedname) {
        this.schemaqualifiedname = schemaqualifiedname;
    }

}