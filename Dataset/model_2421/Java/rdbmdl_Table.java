





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_Table extends NamedColumnSet {






    private List<rdbmdl_TableColumn> rdbmdl_tablecolumns;


    public rdbmdl_Table(
    ) {
        super(
        );
        this.rdbmdl_tablecolumns = new ArrayList<>();
    }

    public rdbmdl_Table(
        ArrayList<rdbmdl_TableColumn> rdbmdl_tablecolumns    ) {
        this.rdbmdl_tablecolumns = rdbmdl_tablecolumns;
    }


    public List<rdbmdl_TableColumn> getRdbmdl_tablecolumns() {
        return rdbmdl_tablecolumns;
    }

    public void addRdbmdl_tablecolumn(Rdbmdl_tablecolumn rdbmdl_tablecolumn) {
        this.rdbmdl_tablecolumns.add(rdbmdl_tablecolumn);
    }

}