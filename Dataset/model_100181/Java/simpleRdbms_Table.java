





import java.util.List;
import java.util.ArrayList;

public class simpleRdbms_Table extends RModelElement {






    private simpleRdbms_Schema simplerdbms_schema;




    private List<simpleRdbms_ForeignKey> simplerdbms_foreignkeys;




    private simpleRdbms_Schema simplerdbms_schema;




    private simpleRdbms_Key simplerdbms_key;




    private List<simpleRdbms_Key> simplerdbms_keys;




    private simpleRdbms_ForeignKey simplerdbms_foreignkey;


    public simpleRdbms_Table(
    ) {
        super(
        );
        this.simplerdbms_foreignkeys = new ArrayList<>();
        this.simplerdbms_keys = new ArrayList<>();
    }

    public simpleRdbms_Table(
        ArrayList<simpleRdbms_ForeignKey> simplerdbms_foreignkeys,        ArrayList<simpleRdbms_Key> simplerdbms_keys    ) {
        this.simplerdbms_foreignkeys = simplerdbms_foreignkeys;
        this.simplerdbms_keys = simplerdbms_keys;
    }


    public simpleRdbms_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simpleRdbms_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }
    public List<simpleRdbms_ForeignKey> getSimplerdbms_foreignkeys() {
        return simplerdbms_foreignkeys;
    }

    public void addSimplerdbms_foreignkey(Simplerdbms_foreignkey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkeys.add(simplerdbms_foreignkey);
    }
    public simpleRdbms_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simpleRdbms_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }
    public simpleRdbms_Key getSimplerdbms_key() {
        return simplerdbms_key;
    }

    public void setSimplerdbms_key(simpleRdbms_Key simplerdbms_key) {
        this.simplerdbms_key = simplerdbms_key;
    }
    public List<simpleRdbms_Key> getSimplerdbms_keys() {
        return simplerdbms_keys;
    }

    public void addSimplerdbms_key(Simplerdbms_key simplerdbms_key) {
        this.simplerdbms_keys.add(simplerdbms_key);
    }
    public simpleRdbms_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(simpleRdbms_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }

}