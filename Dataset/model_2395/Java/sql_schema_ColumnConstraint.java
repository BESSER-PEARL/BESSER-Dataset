





import java.util.List;
import java.util.ArrayList;

public class sql_schema_ColumnConstraint extends EObject {






    private SchemaQualifiedName schemaqualifiedname;




    private Column column;


    public sql_schema_ColumnConstraint(
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
    public Column getColumn() {
        return column;
    }

    public void setColumn(Column column) {
        this.column = column;
    }

}