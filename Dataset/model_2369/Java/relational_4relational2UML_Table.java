





import java.util.List;
import java.util.ArrayList;

public class relational_4relational2UML_Table extends ModelElement {

    private String name;





    private relational_4relational2UML_Column relational_4relational2uml_column;




    private relational_4relational2UML_Schema relational_4relational2uml_schema;




    private List<relational_4relational2UML_Column> relational_4relational2uml_columns;




    private relational_4relational2UML_Schema relational_4relational2uml_schema;


    public relational_4relational2UML_Table(
        String name    ) {
        super(
        );
        this.name = name;
        this.relational_4relational2uml_columns = new ArrayList<>();
    }

    public relational_4relational2UML_Table(
        String name        ArrayList<relational_4relational2UML_Column> relational_4relational2uml_columns    ) {
        this.name = name;
        this.relational_4relational2uml_columns = relational_4relational2uml_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public relational_4relational2UML_Column getRelational_4relational2uml_column() {
        return relational_4relational2uml_column;
    }

    public void setRelational_4relational2uml_column(relational_4relational2UML_Column relational_4relational2uml_column) {
        this.relational_4relational2uml_column = relational_4relational2uml_column;
    }
    public relational_4relational2UML_Schema getRelational_4relational2uml_schema() {
        return relational_4relational2uml_schema;
    }

    public void setRelational_4relational2uml_schema(relational_4relational2UML_Schema relational_4relational2uml_schema) {
        this.relational_4relational2uml_schema = relational_4relational2uml_schema;
    }
    public List<relational_4relational2UML_Column> getRelational_4relational2uml_columns() {
        return relational_4relational2uml_columns;
    }

    public void addRelational_4relational2uml_column(Relational_4relational2uml_column relational_4relational2uml_column) {
        this.relational_4relational2uml_columns.add(relational_4relational2uml_column);
    }
    public relational_4relational2UML_Schema getRelational_4relational2uml_schema() {
        return relational_4relational2uml_schema;
    }

    public void setRelational_4relational2uml_schema(relational_4relational2UML_Schema relational_4relational2uml_schema) {
        this.relational_4relational2uml_schema = relational_4relational2uml_schema;
    }

}