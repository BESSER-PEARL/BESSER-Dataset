





import java.util.List;
import java.util.ArrayList;

public class relational_Database extends ModelElement {

    private String name;
    private String url;





    private relational_Schema relational_schema;




    private List<relational_Schema> relational_schemas;


    public relational_Database(
        String name,        String url    ) {
        super(
        );
        this.name = name;
        this.url = url;
        this.relational_schemas = new ArrayList<>();
    }

    public relational_Database(
        String name,        String url        ArrayList<relational_Schema> relational_schemas    ) {
        this.name = name;
        this.url = url;
        this.relational_schemas = relational_schemas;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
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

}