





import java.util.List;
import java.util.ArrayList;

public class RDBMS_Column  {

    private String type;
    private String name;





    private List<RDBMS_ForeignKey> rdbms_foreignkeys;




    private RDBMS_Table rdbms_table;




    private RDBMS_ForeignKey rdbms_foreignkey;




    private RDBMS_Table rdbms_table;


    public RDBMS_Column(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.rdbms_foreignkeys = new ArrayList<>();
    }

    public RDBMS_Column(
        String type,        String name        ArrayList<RDBMS_ForeignKey> rdbms_foreignkeys    ) {
        this.type = type;
        this.name = name;
        this.rdbms_foreignkeys = rdbms_foreignkeys;
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

    public List<RDBMS_ForeignKey> getRdbms_foreignkeys() {
        return rdbms_foreignkeys;
    }

    public void addRdbms_foreignkey(Rdbms_foreignkey rdbms_foreignkey) {
        this.rdbms_foreignkeys.add(rdbms_foreignkey);
    }
    public RDBMS_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(RDBMS_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public RDBMS_ForeignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(RDBMS_ForeignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
    }
    public RDBMS_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(RDBMS_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }

}