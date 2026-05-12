





import java.util.List;
import java.util.ArrayList;

public class itm_Role  {

    private String name;
    private String permissions;



    public itm_Role(
        String name,        String permissions    ) {
        this.name = name;
        this.permissions = permissions;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPermissions() {
        return permissions;
    }

    public void setPermissions(String permissions) {
        this.permissions = permissions;
    }


}