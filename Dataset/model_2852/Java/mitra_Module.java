





import java.util.List;
import java.util.ArrayList;

public class mitra_Module  {

    private String packageName;
    private String name;



    public mitra_Module(
        String packageName,        String name    ) {
        this.packageName = packageName;
        this.name = name;
    }


    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}