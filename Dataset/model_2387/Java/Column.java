





import java.util.List;
import java.util.ArrayList;

public class Column  {






    private mm_rdb_PrimaryKey mm_rdb_primarykey;




    private mm_rdb_ForeignKey mm_rdb_foreignkey;




    private mm_rdb_Index mm_rdb_index;


    public Column(
    ) {
    }



    public mm_rdb_PrimaryKey getMm_rdb_primarykey() {
        return mm_rdb_primarykey;
    }

    public void setMm_rdb_primarykey(mm_rdb_PrimaryKey mm_rdb_primarykey) {
        this.mm_rdb_primarykey = mm_rdb_primarykey;
    }
    public mm_rdb_ForeignKey getMm_rdb_foreignkey() {
        return mm_rdb_foreignkey;
    }

    public void setMm_rdb_foreignkey(mm_rdb_ForeignKey mm_rdb_foreignkey) {
        this.mm_rdb_foreignkey = mm_rdb_foreignkey;
    }
    public mm_rdb_Index getMm_rdb_index() {
        return mm_rdb_index;
    }

    public void setMm_rdb_index(mm_rdb_Index mm_rdb_index) {
        this.mm_rdb_index = mm_rdb_index;
    }

}