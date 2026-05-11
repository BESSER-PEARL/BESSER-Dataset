





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Column extends RModelElement {

    private String type;





    private SimpleRDBMS_Key simplerdbms_key;




    private SimpleRDBMS_Table simplerdbms_table;




    private List<SimpleRDBMS_Key> simplerdbms_keys;




    private SimpleRDBMS_Table simplerdbms_table;


    public SimpleRDBMS_Column(
        String type    ) {
        super(
        );
        this.type = type;
        this.simplerdbms_keys = new ArrayList<>();
    }

    public SimpleRDBMS_Column(
        String type        ArrayList<SimpleRDBMS_Key> simplerdbms_keys    ) {
        this.type = type;
        this.simplerdbms_keys = simplerdbms_keys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public SimpleRDBMS_Key getSimplerdbms_key() {
        return simplerdbms_key;
    }

    public void setSimplerdbms_key(SimpleRDBMS_Key simplerdbms_key) {
        this.simplerdbms_key = simplerdbms_key;
    }
    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public List<SimpleRDBMS_Key> getSimplerdbms_keys() {
        return simplerdbms_keys;
    }

    public void addSimplerdbms_key(Simplerdbms_key simplerdbms_key) {
        this.simplerdbms_keys.add(simplerdbms_key);
    }
    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }

}