





import java.util.List;
import java.util.ArrayList;

public class lSGL_EnumItem  {

    private String name;
    private String value;





    private lSGL_Enum lsgl_enum;


    public lSGL_EnumItem(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public lSGL_Enum getLsgl_enum() {
        return lsgl_enum;
    }

    public void setLsgl_enum(lSGL_Enum lsgl_enum) {
        this.lsgl_enum = lsgl_enum;
    }

}