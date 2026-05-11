





import java.util.List;
import java.util.ArrayList;

public class KragsteinPackage_Method  {

    private boolean isVirtual;
    private boolean isStatic;
    private boolean isConst;
    private String visibility;
    private String name;
    private String type;





    private KragsteinPackage_Class kragsteinpackage_class;


    public KragsteinPackage_Method(
        boolean isVirtual,        boolean isStatic,        boolean isConst,        String visibility,        String name,        String type    ) {
        this.isVirtual = isVirtual;
        this.isStatic = isStatic;
        this.isConst = isConst;
        this.visibility = visibility;
        this.name = name;
        this.type = type;
    }


    public boolean getIsvirtual() {
        return isVirtual;
    }

    public void setIsvirtual(boolean isVirtual) {
        this.isVirtual = isVirtual;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }
    public boolean getIsconst() {
        return isConst;
    }

    public void setIsconst(boolean isConst) {
        this.isConst = isConst;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
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

    public KragsteinPackage_Class getKragsteinpackage_class() {
        return kragsteinpackage_class;
    }

    public void setKragsteinpackage_class(KragsteinPackage_Class kragsteinpackage_class) {
        this.kragsteinpackage_class = kragsteinpackage_class;
    }

}