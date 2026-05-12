





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Key extends RModelElement {






    private SimpleRDBMS_Table simplerdbms_table;




    private List<SimpleRDBMS_Column> simplerdbms_columns;




    private SimpleRDBMS_Table simplerdbms_table;




    private SimpleRDBMS_Column simplerdbms_column;




    private SimpleRDBMS_ForeignKey simplerdbms_foreignkey;


    public SimpleRDBMS_Key(
    ) {
        super(
        );
        this.simplerdbms_columns = new ArrayList<>();
    }

    public SimpleRDBMS_Key(
        ArrayList<SimpleRDBMS_Column> simplerdbms_columns    ) {
        this.simplerdbms_columns = simplerdbms_columns;
    }


    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public List<SimpleRDBMS_Column> getSimplerdbms_columns() {
        return simplerdbms_columns;
    }

    public void addSimplerdbms_column(Simplerdbms_column simplerdbms_column) {
        this.simplerdbms_columns.add(simplerdbms_column);
    }
    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public SimpleRDBMS_Column getSimplerdbms_column() {
        return simplerdbms_column;
    }

    public void setSimplerdbms_column(SimpleRDBMS_Column simplerdbms_column) {
        this.simplerdbms_column = simplerdbms_column;
    }
    public SimpleRDBMS_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(SimpleRDBMS_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }

}