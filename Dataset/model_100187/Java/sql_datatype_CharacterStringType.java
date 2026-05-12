





import java.util.List;
import java.util.ArrayList;

public class sql_datatype_CharacterStringType extends PredefinedType {

    private String length;
    private String kind;





    private SchemaQualifiedName schemaqualifiedname;




    private SchemaQualifiedName schemaqualifiedname;


    public sql_datatype_CharacterStringType(
        String length,        String kind    ) {
        super(
        );
        this.length = length;
        this.kind = kind;
    }


    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public SchemaQualifiedName getSchemaqualifiedname() {
        return schemaqualifiedname;
    }

    public void setSchemaqualifiedname(SchemaQualifiedName schemaqualifiedname) {
        this.schemaqualifiedname = schemaqualifiedname;
    }
    public SchemaQualifiedName getSchemaqualifiedname() {
        return schemaqualifiedname;
    }

    public void setSchemaqualifiedname(SchemaQualifiedName schemaqualifiedname) {
        this.schemaqualifiedname = schemaqualifiedname;
    }

}