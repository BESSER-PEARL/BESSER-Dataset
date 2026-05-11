





import java.util.List;
import java.util.ArrayList;

public class ale_ClassifierType extends classifierTypeRule {

    private String packageName;
    private String className;



    public ale_ClassifierType(
        String packageName,        String className    ) {
        super(
        );
        this.packageName = packageName;
        this.className = className;
    }


    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }


}