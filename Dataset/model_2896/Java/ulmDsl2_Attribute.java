





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_Attribute  {

    private String desc;
    private String name;



    public ulmDsl2_Attribute(
        String desc,        String name    ) {
        this.desc = desc;
        this.name = name;
    }


    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}