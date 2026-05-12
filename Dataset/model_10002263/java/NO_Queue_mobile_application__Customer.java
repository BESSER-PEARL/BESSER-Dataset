





import java.util.List;
import java.util.ArrayList;

public class NO_Queue_mobile_application__Customer  {

    private String Phone;
    private String ID;
    private String Email;
    private String Address;





    private NO_Queue_mobile_application__App_User no_queue_mobile_application__app_user;


    public NO_Queue_mobile_application__Customer(
        String Phone,        String ID,        String Email,        String Address    ) {
        this.Phone = Phone;
        this.ID = ID;
        this.Email = Email;
        this.Address = Address;
    }


    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public NO_Queue_mobile_application__App_User getNo_queue_mobile_application__app_user() {
        return no_queue_mobile_application__app_user;
    }

    public void setNo_queue_mobile_application__app_user(NO_Queue_mobile_application__App_User no_queue_mobile_application__app_user) {
        this.no_queue_mobile_application__app_user = no_queue_mobile_application__app_user;
    }

}