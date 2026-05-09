





import java.util.List;
import java.util.ArrayList;

public class vml_Table  {

    private String tableTitle;





    private List<vml_Column> vml_columns;




    private vml_Model vml_model;




    private List<vml_Row> vml_rows;


    public vml_Table(
        String tableTitle    ) {
        this.tableTitle = tableTitle;
        this.vml_columns = new ArrayList<>();
        this.vml_rows = new ArrayList<>();
    }

    public vml_Table(
        String tableTitle        ArrayList<vml_Column> vml_columns,        ArrayList<vml_Row> vml_rows    ) {
        this.tableTitle = tableTitle;
        this.vml_columns = vml_columns;
        this.vml_rows = vml_rows;
    }

    public String getTabletitle() {
        return tableTitle;
    }

    public void setTabletitle(String tableTitle) {
        this.tableTitle = tableTitle;
    }

    public List<vml_Column> getVml_columns() {
        return vml_columns;
    }

    public void addVml_column(Vml_column vml_column) {
        this.vml_columns.add(vml_column);
    }
    public vml_Model getVml_model() {
        return vml_model;
    }

    public void setVml_model(vml_Model vml_model) {
        this.vml_model = vml_model;
    }
    public List<vml_Row> getVml_rows() {
        return vml_rows;
    }

    public void addVml_row(Vml_row vml_row) {
        this.vml_rows.add(vml_row);
    }

}