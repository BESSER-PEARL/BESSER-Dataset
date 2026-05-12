





import java.util.List;
import java.util.ArrayList;

public class Package_User_Permissions  {

    private String attribute2;
    private String attribute;





    private Package_User_groups package_user_groups;


    public Package_User_Permissions(
        String attribute2,        String attribute    ) {
        this.attribute2 = attribute2;
        this.attribute = attribute;
    }


    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Package_User_groups getPackage_user_groups() {
        return package_user_groups;
    }

    public void setPackage_user_groups(Package_User_groups package_user_groups) {
        this.package_user_groups = package_user_groups;
    }

}