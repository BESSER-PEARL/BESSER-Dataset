





import java.util.List;
import java.util.ArrayList;

public class simpleRDBMS_Table extends NamedElement {






    private List<simpleRDBMS_ForeignKey> simplerdbms_foreignkeys;




    private simpleRDBMS_Schema simplerdbms_schema;


    public simpleRDBMS_Table(
    ) {
        super(
        );
        this.simplerdbms_foreignkeys = new ArrayList<>();
    }

    public simpleRDBMS_Table(
        ArrayList<simpleRDBMS_ForeignKey> simplerdbms_foreignkeys    ) {
        this.simplerdbms_foreignkeys = simplerdbms_foreignkeys;
    }


    public List<simpleRDBMS_ForeignKey> getSimplerdbms_foreignkeys() {
        return simplerdbms_foreignkeys;
    }

    public void addSimplerdbms_foreignkey(Simplerdbms_foreignkey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkeys.add(simplerdbms_foreignkey);
    }
    public simpleRDBMS_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simpleRDBMS_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }

}