





import java.util.List;
import java.util.ArrayList;

public class webapp_Validator  {

    private String package;
    private String name;



    public webapp_Validator(
        String package,        String name    ) {
        this.package = package;
        this.name = name;
    }


    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}