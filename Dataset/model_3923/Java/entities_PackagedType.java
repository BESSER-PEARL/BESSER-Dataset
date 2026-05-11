





import java.util.List;
import java.util.ArrayList;

public class entities_PackagedType  {

    private String name;





    private entities_Package entities_package;


    public entities_PackagedType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entities_Package getEntities_package() {
        return entities_package;
    }

    public void setEntities_package(entities_Package entities_package) {
        this.entities_package = entities_package;
    }

}