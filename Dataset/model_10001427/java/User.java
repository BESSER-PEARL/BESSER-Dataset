





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String email;
    private String User_name;
    private String Card_info;
    private String shipping_info;
    private String address;
    private int phone_no;



    public User(
        String email,        String User_name,        String Card_info,        String shipping_info,        String address,        int phone_no    ) {
        this.email = email;
        this.User_name = User_name;
        this.Card_info = Card_info;
        this.shipping_info = shipping_info;
        this.address = address;
        this.phone_no = phone_no;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUser_name() {
        return User_name;
    }

    public void setUser_name(String User_name) {
        this.User_name = User_name;
    }
    public String getCard_info() {
        return Card_info;
    }

    public void setCard_info(String Card_info) {
        this.Card_info = Card_info;
    }
    public String getShipping_info() {
        return shipping_info;
    }

    public void setShipping_info(String shipping_info) {
        this.shipping_info = shipping_info;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(int phone_no) {
        this.phone_no = phone_no;
    }


}