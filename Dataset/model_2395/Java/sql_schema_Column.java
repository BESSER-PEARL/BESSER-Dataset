





import java.util.List;
import java.util.ArrayList;

public class sql_schema_Column extends TableElement {

    private String name;





    private DataType datatype;




    private SchemaQualifiedName schemaqualifiedname;


    public sql_schema_Column(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DataType getDatatype() {
        return datatype;
    }

    public void setDatatype(DataType datatype) {
        this.datatype = datatype;
    }
    public SchemaQualifiedName getSchemaqualifiedname() {
        return schemaqualifiedname;
    }

    public void setSchemaqualifiedname(SchemaQualifiedName schemaqualifiedname) {
        this.schemaqualifiedname = schemaqualifiedname;
    }

}