





import java.util.List;
import java.util.ArrayList;

public class beans_BeanLibrary extends NamedElement {

    private String packageName;



    public beans_BeanLibrary(
        String packageName    ) {
        super(
        );
        this.packageName = packageName;
    }


    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }


}