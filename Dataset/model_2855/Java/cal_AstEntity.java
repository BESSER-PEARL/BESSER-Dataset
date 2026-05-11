





import java.util.List;
import java.util.ArrayList;

public class cal_AstEntity  {

    private String name;
    private String package;



    public cal_AstEntity(
        String name,        String package    ) {
        this.name = name;
        this.package = package;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }


}