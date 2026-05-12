





import java.util.List;
import java.util.ArrayList;

public class TableColumn  {






    private mm_rdb_Table mm_rdb_table;




    private mm_rdb_Index mm_rdb_index;




    private mm_rdb_ForeignKey mm_rdb_foreignkey;


    public TableColumn(
    ) {
    }



    public mm_rdb_Table getMm_rdb_table() {
        return mm_rdb_table;
    }

    public void setMm_rdb_table(mm_rdb_Table mm_rdb_table) {
        this.mm_rdb_table = mm_rdb_table;
    }
    public mm_rdb_Index getMm_rdb_index() {
        return mm_rdb_index;
    }

    public void setMm_rdb_index(mm_rdb_Index mm_rdb_index) {
        this.mm_rdb_index = mm_rdb_index;
    }
    public mm_rdb_ForeignKey getMm_rdb_foreignkey() {
        return mm_rdb_foreignkey;
    }

    public void setMm_rdb_foreignkey(mm_rdb_ForeignKey mm_rdb_foreignkey) {
        this.mm_rdb_foreignkey = mm_rdb_foreignkey;
    }

}