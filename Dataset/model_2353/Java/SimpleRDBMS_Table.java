





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Table extends RModelElement {






    private List<SimpleRDBMS_Key> simplerdbms_keys;




    private SimpleRDBMS_Key simplerdbms_key;


    public SimpleRDBMS_Table(
    ) {
        super(
        );
        this.simplerdbms_keys = new ArrayList<>();
    }

    public SimpleRDBMS_Table(
        ArrayList<SimpleRDBMS_Key> simplerdbms_keys    ) {
        this.simplerdbms_keys = simplerdbms_keys;
    }


    public List<SimpleRDBMS_Key> getSimplerdbms_keys() {
        return simplerdbms_keys;
    }

    public void addSimplerdbms_key(Simplerdbms_key simplerdbms_key) {
        this.simplerdbms_keys.add(simplerdbms_key);
    }
    public SimpleRDBMS_Key getSimplerdbms_key() {
        return simplerdbms_key;
    }

    public void setSimplerdbms_key(SimpleRDBMS_Key simplerdbms_key) {
        this.simplerdbms_key = simplerdbms_key;
    }

}