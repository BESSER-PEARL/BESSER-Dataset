





import java.util.List;
import java.util.ArrayList;

public class umltordbms_ClassToTable extends ToColumn, FromAttributeOwner {

    private String name;





    private umltordbms_Table umltordbms_table;




    private umltordbms_Key umltordbms_key;


    public umltordbms_ClassToTable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umltordbms_Table getUmltordbms_table() {
        return umltordbms_table;
    }

    public void setUmltordbms_table(umltordbms_Table umltordbms_table) {
        this.umltordbms_table = umltordbms_table;
    }
    public umltordbms_Key getUmltordbms_key() {
        return umltordbms_key;
    }

    public void setUmltordbms_key(umltordbms_Key umltordbms_key) {
        this.umltordbms_key = umltordbms_key;
    }

}