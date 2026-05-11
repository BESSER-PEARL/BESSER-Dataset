





import java.util.List;
import java.util.ArrayList;

public class SOS_set_ModelSort extends Sort {

    private String className;
    private String packageName;



    public SOS_set_ModelSort(
        String className,        String packageName    ) {
        super(
        );
        this.className = className;
        this.packageName = packageName;
    }


    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }


}