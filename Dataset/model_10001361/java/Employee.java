





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private int Mobile_number;
    private int Remaining_days;
    private String First_name;
    private int ID;
    private int Functional_number;
    private String Email_address;
    private String Last_name;





    private Admin admin;


    public Employee(
        int Mobile_number,        int Remaining_days,        String First_name,        int ID,        int Functional_number,        String Email_address,        String Last_name    ) {
        this.Mobile_number = Mobile_number;
        this.Remaining_days = Remaining_days;
        this.First_name = First_name;
        this.ID = ID;
        this.Functional_number = Functional_number;
        this.Email_address = Email_address;
        this.Last_name = Last_name;
    }


    public int getMobile_number() {
        return Mobile_number;
    }

    public void setMobile_number(int Mobile_number) {
        this.Mobile_number = Mobile_number;
    }
    public int getRemaining_days() {
        return Remaining_days;
    }

    public void setRemaining_days(int Remaining_days) {
        this.Remaining_days = Remaining_days;
    }
    public String getFirst_name() {
        return First_name;
    }

    public void setFirst_name(String First_name) {
        this.First_name = First_name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getFunctional_number() {
        return Functional_number;
    }

    public void setFunctional_number(int Functional_number) {
        this.Functional_number = Functional_number;
    }
    public String getEmail_address() {
        return Email_address;
    }

    public void setEmail_address(String Email_address) {
        this.Email_address = Email_address;
    }
    public String getLast_name() {
        return Last_name;
    }

    public void setLast_name(String Last_name) {
        this.Last_name = Last_name;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}