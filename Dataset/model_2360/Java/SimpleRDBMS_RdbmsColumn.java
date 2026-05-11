





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsColumn extends RdbmsModelElement {

    private String rdbmsType;





    private SimpleRDBMS_RdbmsForeignKey simplerdbms_rdbmsforeignkey;




    private List<SimpleRDBMS_RdbmsForeignKey> simplerdbms_rdbmsforeignkeys;


    public SimpleRDBMS_RdbmsColumn(
        String rdbmsType    ) {
        super(
        );
        this.rdbmsType = rdbmsType;
        this.simplerdbms_rdbmsforeignkeys = new ArrayList<>();
    }

    public SimpleRDBMS_RdbmsColumn(
        String rdbmsType        ArrayList<SimpleRDBMS_RdbmsForeignKey> simplerdbms_rdbmsforeignkeys    ) {
        this.rdbmsType = rdbmsType;
        this.simplerdbms_rdbmsforeignkeys = simplerdbms_rdbmsforeignkeys;
    }

    public String getRdbmstype() {
        return rdbmsType;
    }

    public void setRdbmstype(String rdbmsType) {
        this.rdbmsType = rdbmsType;
    }

    public SimpleRDBMS_RdbmsForeignKey getSimplerdbms_rdbmsforeignkey() {
        return simplerdbms_rdbmsforeignkey;
    }

    public void setSimplerdbms_rdbmsforeignkey(SimpleRDBMS_RdbmsForeignKey simplerdbms_rdbmsforeignkey) {
        this.simplerdbms_rdbmsforeignkey = simplerdbms_rdbmsforeignkey;
    }
    public List<SimpleRDBMS_RdbmsForeignKey> getSimplerdbms_rdbmsforeignkeys() {
        return simplerdbms_rdbmsforeignkeys;
    }

    public void addSimplerdbms_rdbmsforeignkey(Simplerdbms_rdbmsforeignkey simplerdbms_rdbmsforeignkey) {
        this.simplerdbms_rdbmsforeignkeys.add(simplerdbms_rdbmsforeignkey);
    }

}