





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private None Name;
    private String Privilege;



    public Administrator(
        None Name,        String Privilege    ) {
        this.Name = Name;
        this.Privilege = Privilege;
    }


    public None getName() {
        return Name;
    }

    public void setName(None Name) {
        this.Name = Name;
    }
    public String getPrivilege() {
        return Privilege;
    }

    public void setPrivilege(String Privilege) {
        this.Privilege = Privilege;
    }


}