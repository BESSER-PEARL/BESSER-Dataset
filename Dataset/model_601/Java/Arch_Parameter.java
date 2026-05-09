





import java.util.List;
import java.util.ArrayList;

public class Arch_Parameter  {

    private String name;
    private String type;





    private Arch_Method arch_method;


    public Arch_Parameter(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
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

    public Arch_Method getArch_method() {
        return arch_method;
    }

    public void setArch_method(Arch_Method arch_method) {
        this.arch_method = arch_method;
    }

}