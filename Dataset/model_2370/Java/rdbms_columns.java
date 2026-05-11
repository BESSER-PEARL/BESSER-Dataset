





import java.util.List;
import java.util.ArrayList;

public class rdbms_columns  {

    private String group;





    private List<rdbms_column> rdbms_columns;


    public rdbms_columns(
        String group    ) {
        this.group = group;
        this.rdbms_columns = new ArrayList<>();
    }

    public rdbms_columns(
        String group        ArrayList<rdbms_column> rdbms_columns    ) {
        this.group = group;
        this.rdbms_columns = rdbms_columns;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<rdbms_column> getRdbms_columns() {
        return rdbms_columns;
    }

    public void addRdbms_column(Rdbms_column rdbms_column) {
        this.rdbms_columns.add(rdbms_column);
    }

}