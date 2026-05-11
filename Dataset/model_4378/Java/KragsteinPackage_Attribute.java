





import java.util.List;
import java.util.ArrayList;

public class KragsteinPackage_Attribute  {

    private String name;
    private boolean isConst;
    private String value;
    private boolean isStatic;
    private String type;
    private String visibility;





    private KragsteinPackage_Class kragsteinpackage_class;


    public KragsteinPackage_Attribute(
        String name,        boolean isConst,        String value,        boolean isStatic,        String type,        String visibility    ) {
        this.name = name;
        this.isConst = isConst;
        this.value = value;
        this.isStatic = isStatic;
        this.type = type;
        this.visibility = visibility;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsconst() {
        return isConst;
    }

    public void setIsconst(boolean isConst) {
        this.isConst = isConst;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public KragsteinPackage_Class getKragsteinpackage_class() {
        return kragsteinpackage_class;
    }

    public void setKragsteinpackage_class(KragsteinPackage_Class kragsteinpackage_class) {
        this.kragsteinpackage_class = kragsteinpackage_class;
    }

}