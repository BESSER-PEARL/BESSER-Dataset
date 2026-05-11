





import java.util.List;
import java.util.ArrayList;

public class sql_schema_TableConstraint extends schema_TableElement, EObject {






    private SchemaQualifiedName schemaqualifiedname;


    public sql_schema_TableConstraint(
    ) {
        super(
        );
    }



    public SchemaQualifiedName getSchemaqualifiedname() {
        return schemaqualifiedname;
    }

    public void setSchemaqualifiedname(SchemaQualifiedName schemaqualifiedname) {
        this.schemaqualifiedname = schemaqualifiedname;
    }

}