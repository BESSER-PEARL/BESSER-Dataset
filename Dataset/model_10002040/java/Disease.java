





import java.util.List;
import java.util.ArrayList;

public class Disease  {

    private String name;
    private int code;
    private String type;



    public Disease(
        String name,        int code,        String type    ) {
        this.name = name;
        this.code = code;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}