





import java.util.List;
import java.util.ArrayList;

public class product  {

    private int id;
    private None group;
    private None name;
    private None subgroub;





    private admin admin;




    private customer customer;


    public product(
        int id,        None group,        None name,        None subgroub    ) {
        this.id = id;
        this.group = group;
        this.name = name;
        this.subgroub = subgroub;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getGroup() {
        return group;
    }

    public void setGroup(None group) {
        this.group = group;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }
    public None getSubgroub() {
        return subgroub;
    }

    public void setSubgroub(None subgroub) {
        this.subgroub = subgroub;
    }

    public admin getAdmin() {
        return admin;
    }

    public void setAdmin(admin admin) {
        this.admin = admin;
    }
    public customer getCustomer() {
        return customer;
    }

    public void setCustomer(customer customer) {
        this.customer = customer;
    }

}