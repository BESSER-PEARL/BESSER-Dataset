





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int password;
    private String Name;
    private String address;
    private String mail_id;
    private int phn_no;
    private int id;





    private Guest guest;


    public User(
        int password,        String Name,        String address,        String mail_id,        int phn_no,        int id    ) {
        this.password = password;
        this.Name = Name;
        this.address = address;
        this.mail_id = mail_id;
        this.phn_no = phn_no;
        this.id = id;
    }


    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getMail_id() {
        return mail_id;
    }

    public void setMail_id(String mail_id) {
        this.mail_id = mail_id;
    }
    public int getPhn_no() {
        return phn_no;
    }

    public void setPhn_no(int phn_no) {
        this.phn_no = phn_no;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Guest getGuest() {
        return guest;
    }

    public void setGuest(Guest guest) {
        this.guest = guest;
    }

}