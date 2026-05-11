





import java.util.List;
import java.util.ArrayList;

public class rdb_Schema extends NamedElement {






    private List<rdb_SchemaElement> rdb_schemaelements;




    private rdb_Model rdb_model;


    public rdb_Schema(
    ) {
        super(
        );
        this.rdb_schemaelements = new ArrayList<>();
    }

    public rdb_Schema(
        ArrayList<rdb_SchemaElement> rdb_schemaelements    ) {
        this.rdb_schemaelements = rdb_schemaelements;
    }


    public List<rdb_SchemaElement> getRdb_schemaelements() {
        return rdb_schemaelements;
    }

    public void addRdb_schemaelement(Rdb_schemaelement rdb_schemaelement) {
        this.rdb_schemaelements.add(rdb_schemaelement);
    }
    public rdb_Model getRdb_model() {
        return rdb_model;
    }

    public void setRdb_model(rdb_Model rdb_model) {
        this.rdb_model = rdb_model;
    }

}