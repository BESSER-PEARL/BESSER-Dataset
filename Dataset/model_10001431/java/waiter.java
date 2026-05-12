





import java.util.List;
import java.util.ArrayList;

public class waiter  {

    private int Staffid;
    private String name;





    private chef chef;




    private menu menu;




    private staff staff;


    public waiter(
        int Staffid,        String name    ) {
        this.Staffid = Staffid;
        this.name = name;
    }


    public int getStaffid() {
        return Staffid;
    }

    public void setStaffid(int Staffid) {
        this.Staffid = Staffid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public chef getChef() {
        return chef;
    }

    public void setChef(chef chef) {
        this.chef = chef;
    }
    public menu getMenu() {
        return menu;
    }

    public void setMenu(menu menu) {
        this.menu = menu;
    }
    public staff getStaff() {
        return staff;
    }

    public void setStaff(staff staff) {
        this.staff = staff;
    }

}