





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String nameCustomer;
    private String phoneCustomer;
    private String emailCustomer;
    private int idCustomer;



    public Customer(
        String nameCustomer,        String phoneCustomer,        String emailCustomer,        int idCustomer    ) {
        this.nameCustomer = nameCustomer;
        this.phoneCustomer = phoneCustomer;
        this.emailCustomer = emailCustomer;
        this.idCustomer = idCustomer;
    }


    public String getNamecustomer() {
        return nameCustomer;
    }

    public void setNamecustomer(String nameCustomer) {
        this.nameCustomer = nameCustomer;
    }
    public String getPhonecustomer() {
        return phoneCustomer;
    }

    public void setPhonecustomer(String phoneCustomer) {
        this.phoneCustomer = phoneCustomer;
    }
    public String getEmailcustomer() {
        return emailCustomer;
    }

    public void setEmailcustomer(String emailCustomer) {
        this.emailCustomer = emailCustomer;
    }
    public int getIdcustomer() {
        return idCustomer;
    }

    public void setIdcustomer(int idCustomer) {
        this.idCustomer = idCustomer;
    }


}