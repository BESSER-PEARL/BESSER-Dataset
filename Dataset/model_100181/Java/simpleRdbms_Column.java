





import java.util.List;
import java.util.ArrayList;

public class simpleRdbms_Column extends RModelElement {

    private String type;





    private simpleRdbms_Key simplerdbms_key;




    private List<simpleRdbms_Key> simplerdbms_keys;




    private simpleRdbms_Table simplerdbms_table;




    private simpleRdbms_Table simplerdbms_table;




    private simpleRdbms_ForeignKey simplerdbms_foreignkey;




    private List<simpleRdbms_ForeignKey> simplerdbms_foreignkeys;


    public simpleRdbms_Column(
        String type    ) {
        super(
        );
        this.type = type;
        this.simplerdbms_keys = new ArrayList<>();
        this.simplerdbms_foreignkeys = new ArrayList<>();
    }

    public simpleRdbms_Column(
        String type        ArrayList<simpleRdbms_Key> simplerdbms_keys,        ArrayList<simpleRdbms_ForeignKey> simplerdbms_foreignkeys    ) {
        this.type = type;
        this.simplerdbms_keys = simplerdbms_keys;
        this.simplerdbms_foreignkeys = simplerdbms_foreignkeys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public simpleRdbms_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(simpleRdbms_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public simpleRdbms_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(simpleRdbms_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public simpleRdbms_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(simpleRdbms_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }
    public List<simpleRdbms_ForeignKey> getSimplerdbms_foreignkeys() {
        return simplerdbms_foreignkeys;
    }

    public void addSimplerdbms_foreignkey(Simplerdbms_foreignkey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkeys.add(simplerdbms_foreignkey);
    }

}