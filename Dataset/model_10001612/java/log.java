





import java.util.List;
import java.util.ArrayList;

public class log  {






    private List<Admin> admins;


    public log(
    ) {
        this.admins = new ArrayList<>();
    }

    public log(
        ArrayList<Admin> admins    ) {
        this.admins = admins;
    }


    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}