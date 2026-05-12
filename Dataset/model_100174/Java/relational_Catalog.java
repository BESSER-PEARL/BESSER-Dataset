





import java.util.List;
import java.util.ArrayList;

public class relational_Catalog extends RelationalEntity {






    private relational_Schema relational_schema;




    private List<relational_Schema> relational_schemas;




    private List<relational_Table> relational_tables;




    private relational_Table relational_table;


    public relational_Catalog(
    ) {
        super(
        );
        this.relational_schemas = new ArrayList<>();
        this.relational_tables = new ArrayList<>();
    }

    public relational_Catalog(
        ArrayList<relational_Schema> relational_schemas,        ArrayList<relational_Table> relational_tables    ) {
        this.relational_schemas = relational_schemas;
        this.relational_tables = relational_tables;
    }


    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public List<relational_Schema> getRelational_schemas() {
        return relational_schemas;
    }

    public void addRelational_schema(Relational_schema relational_schema) {
        this.relational_schemas.add(relational_schema);
    }
    public List<relational_Table> getRelational_tables() {
        return relational_tables;
    }

    public void addRelational_table(Relational_table relational_table) {
        this.relational_tables.add(relational_table);
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}