





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_RenameTable extends Operation {

    private String newName;



    public mm_rdb_RenameTable(
        String newName    ) {
        super(
        );
        this.newName = newName;
    }


    public String getNewname() {
        return newName;
    }

    public void setNewname(String newName) {
        this.newName = newName;
    }


}