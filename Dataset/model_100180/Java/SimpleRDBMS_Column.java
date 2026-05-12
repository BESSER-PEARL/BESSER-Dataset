





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Column extends RModelElement {

    private String type;





    private SimpleRDBMS_ForeignKey simplerdbms_foreignkey;




    private List<SimpleRDBMS_ForeignKey> simplerdbms_foreignkeys;




    private SimpleRDBMS_Table simplerdbms_table;




    private SimpleRDBMS_Table simplerdbms_table;


    public SimpleRDBMS_Column(
        String type    ) {
        super(
        );
        this.type = type;
        this.simplerdbms_foreignkeys = new ArrayList<>();
    }

    public SimpleRDBMS_Column(
        String type        ArrayList<SimpleRDBMS_ForeignKey> simplerdbms_foreignkeys    ) {
        this.type = type;
        this.simplerdbms_foreignkeys = simplerdbms_foreignkeys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public SimpleRDBMS_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(SimpleRDBMS_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }
    public List<SimpleRDBMS_ForeignKey> getSimplerdbms_foreignkeys() {
        return simplerdbms_foreignkeys;
    }

    public void addSimplerdbms_foreignkey(Simplerdbms_foreignkey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkeys.add(simplerdbms_foreignkey);
    }
    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }

}