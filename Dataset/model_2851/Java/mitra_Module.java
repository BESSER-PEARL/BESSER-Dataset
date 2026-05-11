





import java.util.List;
import java.util.ArrayList;

public class mitra_Module  {

    private String name;
    private String packageName;



    public mitra_Module(
        String name,        String packageName    ) {
        this.name = name;
        this.packageName = packageName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }


}