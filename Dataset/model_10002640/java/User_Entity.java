





import java.util.List;
import java.util.ArrayList;

public class User_Entity  {

    private String password;
    private String Email;
    private String login;
    private String City;





    private PostStay_Entity poststay_entity;




    private Booking_Entity booking_entity;


    public User_Entity(
        String password,        String Email,        String login,        String City    ) {
        this.password = password;
        this.Email = Email;
        this.login = login;
        this.City = City;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }

    public PostStay_Entity getPoststay_entity() {
        return poststay_entity;
    }

    public void setPoststay_entity(PostStay_Entity poststay_entity) {
        this.poststay_entity = poststay_entity;
    }
    public Booking_Entity getBooking_entity() {
        return booking_entity;
    }

    public void setBooking_entity(Booking_Entity booking_entity) {
        this.booking_entity = booking_entity;
    }

}