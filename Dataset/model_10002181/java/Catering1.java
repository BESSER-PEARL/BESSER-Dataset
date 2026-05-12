





import java.util.List;
import java.util.ArrayList;

public class Catering1  {

    private String Menu;
    private String attribute;





    private List<Menu1> menu1s;




    private List<Customer1> customer1s;


    public Catering1(
        String Menu,        String attribute    ) {
        this.Menu = Menu;
        this.attribute = attribute;
        this.menu1s = new ArrayList<>();
        this.customer1s = new ArrayList<>();
    }

    public Catering1(
        String Menu,        String attribute        ArrayList<Menu1> menu1s,        ArrayList<Customer1> customer1s    ) {
        this.Menu = Menu;
        this.attribute = attribute;
        this.menu1s = menu1s;
        this.customer1s = customer1s;
    }

    public String getMenu() {
        return Menu;
    }

    public void setMenu(String Menu) {
        this.Menu = Menu;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public List<Menu1> getMenu1s() {
        return menu1s;
    }

    public void addMenu1(Menu1 menu1) {
        this.menu1s.add(menu1);
    }
    public List<Customer1> getCustomer1s() {
        return customer1s;
    }

    public void addCustomer1(Customer1 customer1) {
        this.customer1s.add(customer1);
    }

}