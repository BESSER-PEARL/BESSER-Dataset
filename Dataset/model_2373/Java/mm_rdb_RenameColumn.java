





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_RenameColumn extends Operation {

    private String newColumnName;



    public mm_rdb_RenameColumn(
        String newColumnName    ) {
        super(
        );
        this.newColumnName = newColumnName;
    }


    public String getNewcolumnname() {
        return newColumnName;
    }

    public void setNewcolumnname(String newColumnName) {
        this.newColumnName = newColumnName;
    }


}