





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Column  {

    private String name;
    private String type;
    private int id;





    private SimpleRDBMS_Table simplerdbms_table;




    private SimpleRDBMS_FKey simplerdbms_fkey;




    private SimpleRDBMS_Table simplerdbms_table;


    public SimpleRDBMS_Column(
        String name,        String type,        int id    ) {
        this.name = name;
        this.type = type;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
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

}