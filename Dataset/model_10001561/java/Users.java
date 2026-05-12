





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private String first_name;
    private int user_phone_no;
    private String user_addr_city;
    private String user_address1;
    private String user_address;
    private int last_name;
    private String user_addr_state;
    private String user_mail;
    private String user_role;



    public Users(
        String first_name,        int user_phone_no,        String user_addr_city,        String user_address1,        String user_address,        int last_name,        String user_addr_state,        String user_mail,        String user_role    ) {
        this.first_name = first_name;
        this.user_phone_no = user_phone_no;
        this.user_addr_city = user_addr_city;
        this.user_address1 = user_address1;
        this.user_address = user_address;
        this.last_name = last_name;
        this.user_addr_state = user_addr_state;
        this.user_mail = user_mail;
        this.user_role = user_role;
    }


    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public int getUser_phone_no() {
        return user_phone_no;
    }

    public void setUser_phone_no(int user_phone_no) {
        this.user_phone_no = user_phone_no;
    }
    public String getUser_addr_city() {
        return user_addr_city;
    }

    public void setUser_addr_city(String user_addr_city) {
        this.user_addr_city = user_addr_city;
    }
    public String getUser_address1() {
        return user_address1;
    }

    public void setUser_address1(String user_address1) {
        this.user_address1 = user_address1;
    }
    public String getUser_address() {
        return user_address;
    }

    public void setUser_address(String user_address) {
        this.user_address = user_address;
    }
    public int getLast_name() {
        return last_name;
    }

    public void setLast_name(int last_name) {
        this.last_name = last_name;
    }
    public String getUser_addr_state() {
        return user_addr_state;
    }

    public void setUser_addr_state(String user_addr_state) {
        this.user_addr_state = user_addr_state;
    }
    public String getUser_mail() {
        return user_mail;
    }

    public void setUser_mail(String user_mail) {
        this.user_mail = user_mail;
    }
    public String getUser_role() {
        return user_role;
    }

    public void setUser_role(String user_role) {
        this.user_role = user_role;
    }


}