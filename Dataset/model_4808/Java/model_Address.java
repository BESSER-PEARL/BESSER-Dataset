





import java.util.List;
import java.util.ArrayList;

public class model_Address  {

    private String addId;
    private String street;
    private String city;
    private String number;





    private model_User model_user;


    public model_Address(
        String addId,        String street,        String city,        String number    ) {
        this.addId = addId;
        this.street = street;
        this.city = city;
        this.number = number;
    }


    public String getAddid() {
        return addId;
    }

    public void setAddid(String addId) {
        this.addId = addId;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public model_User getModel_user() {
        return model_user;
    }

    public void setModel_user(model_User model_user) {
        this.model_user = model_user;
    }

}