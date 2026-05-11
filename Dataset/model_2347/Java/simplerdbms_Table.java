





import java.util.List;
import java.util.ArrayList;

public class simplerdbms_Table extends RModelElement {






    private simplerdbms_Schema simplerdbms_schema;




    private List<simplerdbms_Column> simplerdbms_columns;




    private simplerdbms_Column simplerdbms_column;




    private simplerdbms_Schema simplerdbms_schema;


    public simplerdbms_Table(
    ) {
        super(
        );
        this.simplerdbms_columns = new ArrayList<>();
    }

    public simplerdbms_Table(
        ArrayList<simplerdbms_Column> simplerdbms_columns    ) {
        this.simplerdbms_columns = simplerdbms_columns;
    }


    public simplerdbms_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simplerdbms_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }
    public List<simplerdbms_Column> getSimplerdbms_columns() {
        return simplerdbms_columns;
    }

    public void addSimplerdbms_column(Simplerdbms_column simplerdbms_column) {
        this.simplerdbms_columns.add(simplerdbms_column);
    }
    public simplerdbms_Column getSimplerdbms_column() {
        return simplerdbms_column;
    }

    public void setSimplerdbms_column(simplerdbms_Column simplerdbms_column) {
        this.simplerdbms_column = simplerdbms_column;
    }
    public simplerdbms_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simplerdbms_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }

}