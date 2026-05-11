





import java.util.List;
import java.util.ArrayList;

public class UniqueConstraint  {






    private rdb_Table rdb_table;




    private rdb_constraints_ForeignKey rdb_constraints_foreignkey;


    public UniqueConstraint(
    ) {
    }



    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }
    public rdb_constraints_ForeignKey getRdb_constraints_foreignkey() {
        return rdb_constraints_foreignkey;
    }

    public void setRdb_constraints_foreignkey(rdb_constraints_ForeignKey rdb_constraints_foreignkey) {
        this.rdb_constraints_foreignkey = rdb_constraints_foreignkey;
    }

}