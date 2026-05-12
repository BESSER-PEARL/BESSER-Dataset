





import java.util.List;
import java.util.ArrayList;

public class menu  {

    private int Price;
    private String Menuname;
    private String Menuid;





    private staff staff;




    private customer customer;


    public menu(
        int Price,        String Menuname,        String Menuid    ) {
        this.Price = Price;
        this.Menuname = Menuname;
        this.Menuid = Menuid;
    }


    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }
    public String getMenuname() {
        return Menuname;
    }

    public void setMenuname(String Menuname) {
        this.Menuname = Menuname;
    }
    public String getMenuid() {
        return Menuid;
    }

    public void setMenuid(String Menuid) {
        this.Menuid = Menuid;
    }

    public staff getStaff() {
        return staff;
    }

    public void setStaff(staff staff) {
        this.staff = staff;
    }
    public customer getCustomer() {
        return customer;
    }

    public void setCustomer(customer customer) {
        this.customer = customer;
    }

}