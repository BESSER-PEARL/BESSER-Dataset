





import java.util.List;
import java.util.ArrayList;

public class KragsteinPackage_Parameter  {

    private String value;
    private String type;
    private String name;





    private KragsteinPackage_Method kragsteinpackage_method;


    public KragsteinPackage_Parameter(
        String value,        String type,        String name    ) {
        this.value = value;
        this.type = type;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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

    public KragsteinPackage_Method getKragsteinpackage_method() {
        return kragsteinpackage_method;
    }

    public void setKragsteinpackage_method(KragsteinPackage_Method kragsteinpackage_method) {
        this.kragsteinpackage_method = kragsteinpackage_method;
    }

}