





import java.util.List;
import java.util.ArrayList;

public class model_Database extends NamedElement, DescribedElement {

    private String dsn;





    private List<model_Schema> model_schemas;




    private model_Site model_site;


    public model_Database(
        String dsn    ) {
        super(
        );
        this.dsn = dsn;
        this.model_schemas = new ArrayList<>();
    }

    public model_Database(
        String dsn        ArrayList<model_Schema> model_schemas    ) {
        this.dsn = dsn;
        this.model_schemas = model_schemas;
    }

    public String getDsn() {
        return dsn;
    }

    public void setDsn(String dsn) {
        this.dsn = dsn;
    }

    public List<model_Schema> getModel_schemas() {
        return model_schemas;
    }

    public void addModel_schema(Model_schema model_schema) {
        this.model_schemas.add(model_schema);
    }
    public model_Site getModel_site() {
        return model_site;
    }

    public void setModel_site(model_Site model_site) {
        this.model_site = model_site;
    }

}