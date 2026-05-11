





import java.util.List;
import java.util.ArrayList;

public class simplerdbms_Key extends RModelElement {






    private List<simplerdbms_Column> simplerdbms_columns;




    private simplerdbms_Table simplerdbms_table;




    private simplerdbms_Column simplerdbms_column;




    private simplerdbms_Table simplerdbms_table;


    public simplerdbms_Key(
    ) {
        super(
        );
        this.simplerdbms_columns = new ArrayList<>();
    }

    public simplerdbms_Key(
        ArrayList<simplerdbms_Column> simplerdbms_columns    ) {
        this.simplerdbms_columns = simplerdbms_columns;
    }


    public List<simplerdbms_Column> getSimplerdbms_columns() {
        return simplerdbms_columns;
    }

    public void addSimplerdbms_column(Simplerdbms_column simplerdbms_column) {
        this.simplerdbms_columns.add(simplerdbms_column);
    }
    public simplerdbms_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(simplerdbms_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public simplerdbms_Column getSimplerdbms_column() {
        return simplerdbms_column;
    }

    public void setSimplerdbms_column(simplerdbms_Column simplerdbms_column) {
        this.simplerdbms_column = simplerdbms_column;
    }
    public simplerdbms_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(simplerdbms_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }

}