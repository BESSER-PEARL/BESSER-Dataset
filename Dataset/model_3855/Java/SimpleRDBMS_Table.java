





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Table  {

    private String name;
    private int id;





    private List<SimpleRDBMS_FKey> simplerdbms_fkeys;




    private SimpleRDBMS_FKey simplerdbms_fkey;




    private List<SimpleRDBMS_Column> simplerdbms_columns;




    private List<SimpleRDBMS_Column> simplerdbms_columns;


    public SimpleRDBMS_Table(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.simplerdbms_fkeys = new ArrayList<>();
        this.simplerdbms_columns = new ArrayList<>();
        this.simplerdbms_columns = new ArrayList<>();
    }

    public SimpleRDBMS_Table(
        String name,        int id        ArrayList<SimpleRDBMS_FKey> simplerdbms_fkeys,        ArrayList<SimpleRDBMS_Column> simplerdbms_columns,        ArrayList<SimpleRDBMS_Column> simplerdbms_columns    ) {
        this.name = name;
        this.id = id;
        this.simplerdbms_fkeys = simplerdbms_fkeys;
        this.simplerdbms_columns = simplerdbms_columns;
        this.simplerdbms_columns = simplerdbms_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<SimpleRDBMS_FKey> getSimplerdbms_fkeys() {
        return simplerdbms_fkeys;
    }

    public void addSimplerdbms_fkey(Simplerdbms_fkey simplerdbms_fkey) {
        this.simplerdbms_fkeys.add(simplerdbms_fkey);
    }
    public SimpleRDBMS_FKey getSimplerdbms_fkey() {
        return simplerdbms_fkey;
    }

    public void setSimplerdbms_fkey(SimpleRDBMS_FKey simplerdbms_fkey) {
        this.simplerdbms_fkey = simplerdbms_fkey;
    }
    public List<SimpleRDBMS_Column> getSimplerdbms_columns() {
        return simplerdbms_columns;
    }

    public void addSimplerdbms_column(Simplerdbms_column simplerdbms_column) {
        this.simplerdbms_columns.add(simplerdbms_column);
    }
    public List<SimpleRDBMS_Column> getSimplerdbms_columns() {
        return simplerdbms_columns;
    }

    public void addSimplerdbms_column(Simplerdbms_column simplerdbms_column) {
        this.simplerdbms_columns.add(simplerdbms_column);
    }

}