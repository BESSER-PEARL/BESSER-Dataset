





import java.util.List;
import java.util.ArrayList;

public class relational_Table  {

    private String name;





    private List<relational_Field> relational_fields;




    private relational_Schema relational_schema;


    public relational_Table(
        String name    ) {
        this.name = name;
        this.relational_fields = new ArrayList<>();
    }

    public relational_Table(
        String name        ArrayList<relational_Field> relational_fields    ) {
        this.name = name;
        this.relational_fields = relational_fields;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<relational_Field> getRelational_fields() {
        return relational_fields;
    }

    public void addRelational_field(Relational_field relational_field) {
        this.relational_fields.add(relational_field);
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }

}