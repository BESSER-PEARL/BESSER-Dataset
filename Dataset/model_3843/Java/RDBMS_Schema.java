





import java.util.List;
import java.util.ArrayList;

public class RDBMS_Schema  {

    private String name;





    private List<Table> tables;


    public RDBMS_Schema(
        String name    ) {
        this.name = name;
        this.tables = new ArrayList<>();
    }

    public RDBMS_Schema(
        String name        ArrayList<Table> tables    ) {
        this.name = name;
        this.tables = tables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Table> getTables() {
        return tables;
    }

    public void addTable(Table table) {
        this.tables.add(table);
    }

}