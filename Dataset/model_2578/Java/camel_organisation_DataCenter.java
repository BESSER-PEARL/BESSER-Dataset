





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_DataCenter  {

    private String name;
    private String codeName;





    private Location location;


    public camel_organisation_DataCenter(
        String name,        String codeName    ) {
        this.name = name;
        this.codeName = codeName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCodename() {
        return codeName;
    }

    public void setCodename(String codeName) {
        this.codeName = codeName;
    }

    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

}