





import java.util.List;
import java.util.ArrayList;

public class tExp_Together  {






    private List<tExp_Role> texp_roles;




    private tExp_Partition texp_partition;


    public tExp_Together(
    ) {
        this.texp_roles = new ArrayList<>();
    }

    public tExp_Together(
        ArrayList<tExp_Role> texp_roles    ) {
        this.texp_roles = texp_roles;
    }


    public List<tExp_Role> getTexp_roles() {
        return texp_roles;
    }

    public void addTexp_role(Texp_role texp_role) {
        this.texp_roles.add(texp_role);
    }
    public tExp_Partition getTexp_partition() {
        return texp_partition;
    }

    public void setTexp_partition(tExp_Partition texp_partition) {
        this.texp_partition = texp_partition;
    }

}