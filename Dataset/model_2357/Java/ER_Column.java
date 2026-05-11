





import java.util.List;
import java.util.ArrayList;

public class ER_Column  {

    private String type;
    private String name;





    private ER_Table er_table;




    private ER_ForeignKey er_foreignkey;




    private List<ER_ForeignKey> er_foreignkeys;




    private ER_Table er_table;


    public ER_Column(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.er_foreignkeys = new ArrayList<>();
    }

    public ER_Column(
        String type,        String name        ArrayList<ER_ForeignKey> er_foreignkeys    ) {
        this.type = type;
        this.name = name;
        this.er_foreignkeys = er_foreignkeys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public List<ER_ForeignKey> getEr_foreignkeys() {
        return er_foreignkeys;
    }

    public void addEr_foreignkey(Er_foreignkey er_foreignkey) {
        this.er_foreignkeys.add(er_foreignkey);
    }
    public ER_Table getEr_table() {
        return er_table;
    }

    public void setEr_table(ER_Table er_table) {
        this.er_table = er_table;
    }

}