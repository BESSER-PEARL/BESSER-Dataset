





import java.util.List;
import java.util.ArrayList;

public class ConcreteRightAnswers  {

    private String phone;
    private String address;
    private String email;



    public ConcreteRightAnswers(
        String phone,        String address,        String email    ) {
        this.phone = phone;
        this.address = address;
        this.email = email;
    }


    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}