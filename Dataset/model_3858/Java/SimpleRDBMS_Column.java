





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Column  {

    private String name;
    private int id;
    private String type;





    private SimpleRDBMS_FKey simplerdbms_fkey;




    private SimpleRDBMS_Table simplerdbms_table;




    private SimpleRDBMS_Table simplerdbms_table;


    public SimpleRDBMS_Column(
        String name,        int id,        String type    ) {
        this.name = name;
        this.id = id;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public SimpleRDBMS_FKey getSimplerdbms_fkey() {
        return simplerdbms_fkey;
    }

    public void setSimplerdbms_fkey(SimpleRDBMS_FKey simplerdbms_fkey) {
        this.simplerdbms_fkey = simplerdbms_fkey;
    }
    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }

}