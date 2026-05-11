





import java.util.List;
import java.util.ArrayList;

public class programmes_Programme  {

    private String name;
    private String code;



    public programmes_Programme(
        String name,        String code    ) {
        this.name = name;
        this.code = code;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}