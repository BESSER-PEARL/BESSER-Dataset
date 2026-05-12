





import java.util.List;
import java.util.ArrayList;

public class controller  {






    private List<staff_member> staff_members;




    private List<Admin> admins;


    public controller(
    ) {
        this.staff_members = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public controller(
        ArrayList<staff_member> staff_members,        ArrayList<Admin> admins    ) {
        this.staff_members = staff_members;
        this.admins = admins;
    }


    public List<staff_member> getStaff_members() {
        return staff_members;
    }

    public void addStaff_member(Staff_member staff_member) {
        this.staff_members.add(staff_member);
    }
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}