





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Column  {

    private int id;
    private String type;
    private String name;





    private SimpleRDBMS_FKey simplerdbms_fkey;


    public SimpleRDBMS_Column(
        int id,        String type,        String name    ) {
        this.id = id;
        this.type = type;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SimpleRDBMS_FKey getSimplerdbms_fkey() {
        return simplerdbms_fkey;
    }

    public void setSimplerdbms_fkey(SimpleRDBMS_FKey simplerdbms_fkey) {
        this.simplerdbms_fkey = simplerdbms_fkey;
    }

}