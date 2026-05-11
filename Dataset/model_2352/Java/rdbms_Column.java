





import java.util.List;
import java.util.ArrayList;

public class rdbms_Column extends RModelElement {

    private String type;





    private List<rdbms_Key> rdbms_keys;




    private rdbms_Key rdbms_key;


    public rdbms_Column(
        String type    ) {
        super(
        );
        this.type = type;
        this.rdbms_keys = new ArrayList<>();
    }

    public rdbms_Column(
        String type        ArrayList<rdbms_Key> rdbms_keys    ) {
        this.type = type;
        this.rdbms_keys = rdbms_keys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<rdbms_Key> getRdbms_keys() {
        return rdbms_keys;
    }

    public void addRdbms_key(Rdbms_key rdbms_key) {
        this.rdbms_keys.add(rdbms_key);
    }
    public rdbms_Key getRdbms_key() {
        return rdbms_key;
    }

    public void setRdbms_key(rdbms_Key rdbms_key) {
        this.rdbms_key = rdbms_key;
    }

}