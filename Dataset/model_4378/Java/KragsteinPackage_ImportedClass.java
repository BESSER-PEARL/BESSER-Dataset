





import java.util.List;
import java.util.ArrayList;

public class KragsteinPackage_ImportedClass  {

    private String path;
    private boolean isInternal;
    private String name;





    private KragsteinPackage_Class kragsteinpackage_class;


    public KragsteinPackage_ImportedClass(
        String path,        boolean isInternal,        String name    ) {
        this.path = path;
        this.isInternal = isInternal;
        this.name = name;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public boolean getIsinternal() {
        return isInternal;
    }

    public void setIsinternal(boolean isInternal) {
        this.isInternal = isInternal;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public KragsteinPackage_Class getKragsteinpackage_class() {
        return kragsteinpackage_class;
    }

    public void setKragsteinpackage_class(KragsteinPackage_Class kragsteinpackage_class) {
        this.kragsteinpackage_class = kragsteinpackage_class;
    }

}