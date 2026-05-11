





import java.util.List;
import java.util.ArrayList;

public class ER_ForeignKey  {

    private String name;





    private ER_Schema er_schema;




    private ER_Table er_table;




    private ER_Schema er_schema;




    private ER_Table er_table;


    public ER_ForeignKey(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ER_Schema getEr_schema() {
        return er_schema;
    }

    public void setEr_schema(ER_Schema er_schema) {
        this.er_schema = er_schema;
    }
    public ER_Table getEr_table() {
        return er_table;
    }

    public void setEr_table(ER_Table er_table) {
        this.er_table = er_table;
    }
    public ER_Schema getEr_schema() {
        return er_schema;
    }

    public void setEr_schema(ER_Schema er_schema) {
        this.er_schema = er_schema;
    }
    public ER_Table getEr_table() {
        return er_table;
    }

    public void setEr_table(ER_Table er_table) {
        this.er_table = er_table;
    }

}