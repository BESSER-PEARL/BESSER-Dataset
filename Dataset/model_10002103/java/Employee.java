





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String email_id;
    private String paasword;
    private String office_address;
    private String name;
    private int e_id;
    private int phone_no;
    private String address;





    private Admin admin;




    private Admin admin;


    public Employee(
        String email_id,        String paasword,        String office_address,        String name,        int e_id,        int phone_no,        String address    ) {
        this.email_id = email_id;
        this.paasword = paasword;
        this.office_address = office_address;
        this.name = name;
        this.e_id = e_id;
        this.phone_no = phone_no;
        this.address = address;
    }


    public String getEmail_id() {
        return email_id;
    }

    public void setEmail_id(String email_id) {
        this.email_id = email_id;
    }
    public String getPaasword() {
        return paasword;
    }

    public void setPaasword(String paasword) {
        this.paasword = paasword;
    }
    public String getOffice_address() {
        return office_address;
    }

    public void setOffice_address(String office_address) {
        this.office_address = office_address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getE_id() {
        return e_id;
    }

    public void setE_id(int e_id) {
        this.e_id = e_id;
    }
    public int getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(int phone_no) {
        this.phone_no = phone_no;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}