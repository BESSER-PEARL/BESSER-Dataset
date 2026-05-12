





import java.util.List;
import java.util.ArrayList;

public class controller  {






    private List<Admin> admins;




    private List<staff_member> staff_members;


    public controller(
    ) {
        this.admins = new ArrayList<>();
        this.staff_members = new ArrayList<>();
    }

    public controller(
        ArrayList<Admin> admins,        ArrayList<staff_member> staff_members    ) {
        this.admins = admins;
        this.staff_members = staff_members;
    }


    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public List<staff_member> getStaff_members() {
        return staff_members;
    }

    public void addStaff_member(Staff_member staff_member) {
        this.staff_members.add(staff_member);
    }

}