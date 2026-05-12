





import java.util.List;
import java.util.ArrayList;

public class CWMRelationalData_SQLDataType  {

    private String typeNumber;





    private List<Column> columns;


    public CWMRelationalData_SQLDataType(
        String typeNumber    ) {
        this.typeNumber = typeNumber;
        this.columns = new ArrayList<>();
    }

    public CWMRelationalData_SQLDataType(
        String typeNumber        ArrayList<Column> columns    ) {
        this.typeNumber = typeNumber;
        this.columns = columns;
    }

    public String getTypenumber() {
        return typeNumber;
    }

    public void setTypenumber(String typeNumber) {
        this.typeNumber = typeNumber;
    }

    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }

}