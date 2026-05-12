





import java.util.List;
import java.util.ArrayList;

public class rdbms_DocumentRoot  {

    private String mixed;





    private List<rdbms_hasForeignKeys> rdbms_hasforeignkeyss;




    private List<rdbms_referencedKeys> rdbms_referencedkeyss;




    private List<rdbms_column> rdbms_columns;


    public rdbms_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.rdbms_hasforeignkeyss = new ArrayList<>();
        this.rdbms_referencedkeyss = new ArrayList<>();
        this.rdbms_columns = new ArrayList<>();
    }

    public rdbms_DocumentRoot(
        String mixed        ArrayList<rdbms_hasForeignKeys> rdbms_hasforeignkeyss,        ArrayList<rdbms_referencedKeys> rdbms_referencedkeyss,        ArrayList<rdbms_column> rdbms_columns    ) {
        this.mixed = mixed;
        this.rdbms_hasforeignkeyss = rdbms_hasforeignkeyss;
        this.rdbms_referencedkeyss = rdbms_referencedkeyss;
        this.rdbms_columns = rdbms_columns;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<rdbms_hasForeignKeys> getRdbms_hasforeignkeyss() {
        return rdbms_hasforeignkeyss;
    }

    public void addRdbms_hasforeignkeys(Rdbms_hasforeignkeys rdbms_hasforeignkeys) {
        this.rdbms_hasforeignkeyss.add(rdbms_hasforeignkeys);
    }
    public List<rdbms_referencedKeys> getRdbms_referencedkeyss() {
        return rdbms_referencedkeyss;
    }

    public void addRdbms_referencedkeys(Rdbms_referencedkeys rdbms_referencedkeys) {
        this.rdbms_referencedkeyss.add(rdbms_referencedkeys);
    }
    public List<rdbms_column> getRdbms_columns() {
        return rdbms_columns;
    }

    public void addRdbms_column(Rdbms_column rdbms_column) {
        this.rdbms_columns.add(rdbms_column);
    }

}