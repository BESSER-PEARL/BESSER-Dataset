





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_Roles  {






    private List<YasperEPNML114_Role> yasperepnml114_roles;


    public YasperEPNML114_Roles(
    ) {
        this.yasperepnml114_roles = new ArrayList<>();
    }

    public YasperEPNML114_Roles(
        ArrayList<YasperEPNML114_Role> yasperepnml114_roles    ) {
        this.yasperepnml114_roles = yasperepnml114_roles;
    }


    public List<YasperEPNML114_Role> getYasperepnml114_roles() {
        return yasperepnml114_roles;
    }

    public void addYasperepnml114_role(Yasperepnml114_role yasperepnml114_role) {
        this.yasperepnml114_roles.add(yasperepnml114_role);
    }

}