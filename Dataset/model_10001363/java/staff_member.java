





import java.util.List;
import java.util.ArrayList;

public class staff_member  {






    private List<Admin> admins;


    public staff_member(
    ) {
        this.admins = new ArrayList<>();
    }

    public staff_member(
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