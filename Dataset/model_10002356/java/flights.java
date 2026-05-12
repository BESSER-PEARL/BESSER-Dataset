





import java.util.List;
import java.util.ArrayList;

public class flights  {

    private int time;
    private String depart;
    private int number;
    private String name;
    private String dest;





    private List<customer> customers;




    private admin admin;


    public flights(
        int time,        String depart,        int number,        String name,        String dest    ) {
        this.time = time;
        this.depart = depart;
        this.number = number;
        this.name = name;
        this.dest = dest;
        this.customers = new ArrayList<>();
    }

    public flights(
        int time,        String depart,        int number,        String name,        String dest        ArrayList<customer> customers    ) {
        this.time = time;
        this.depart = depart;
        this.number = number;
        this.name = name;
        this.dest = dest;
        this.customers = customers;
    }

    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public String getDepart() {
        return depart;
    }

    public void setDepart(String depart) {
        this.depart = depart;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDest() {
        return dest;
    }

    public void setDest(String dest) {
        this.dest = dest;
    }

    public List<customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }
    public admin getAdmin() {
        return admin;
    }

    public void setAdmin(admin admin) {
        this.admin = admin;
    }

}