





import java.util.List;
import java.util.ArrayList;

public class ER_Key  {

    private String name;





    private List<ER_Column> er_columns;




    private ER_Table er_table;




    private List<ER_ForeignKey> er_foreignkeys;




    private ER_Column er_column;




    private ER_Table er_table;




    private ER_ForeignKey er_foreignkey;


    public ER_Key(
        String name    ) {
        this.name = name;
        this.er_columns = new ArrayList<>();
        this.er_foreignkeys = new ArrayList<>();
    }

    public ER_Key(
        String name        ArrayList<ER_Column> er_columns,        ArrayList<ER_ForeignKey> er_foreignkeys    ) {
        this.name = name;
        this.er_columns = er_columns;
        this.er_foreignkeys = er_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ER_Column> getEr_columns() {
        return er_columns;
    }

    public void addEr_column(Er_column er_column) {
        this.er_columns.add(er_column);
    }
    public ER_Table getEr_table() {
        return er_table;
    }

    public void setEr_table(ER_Table er_table) {
        this.er_table = er_table;
    }
    public List<ER_ForeignKey> getEr_foreignkeys() {
        return er_foreignkeys;
    }

    public void addEr_foreignkey(Er_foreignkey er_foreignkey) {
        this.er_foreignkeys.add(er_foreignkey);
    }
    public ER_Column getEr_column() {
        return er_column;
    }

    public void setEr_column(ER_Column er_column) {
        this.er_column = er_column;
    }
    public ER_Table getEr_table() {
        return er_table;
    }

    public void setEr_table(ER_Table er_table) {
        this.er_table = er_table;
    }
    public ER_ForeignKey getEr_foreignkey() {
        return er_foreignkey;
    }

    public void setEr_foreignkey(ER_ForeignKey er_foreignkey) {
        this.er_foreignkey = er_foreignkey;
    }

}