





import java.util.List;
import java.util.ArrayList;

public class target_Database  {






    private List<target_Table> target_tables;


    public target_Database(
    ) {
        this.target_tables = new ArrayList<>();
    }

    public target_Database(
        ArrayList<target_Table> target_tables    ) {
        this.target_tables = target_tables;
    }


    public List<target_Table> getTarget_tables() {
        return target_tables;
    }

    public void addTarget_table(Target_table target_table) {
        this.target_tables.add(target_table);
    }

}