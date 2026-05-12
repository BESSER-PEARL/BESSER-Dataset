





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String adress;
    private int cardId;
    private String Name;
    private String phone;
    private String email;



    public Customer(
        String adress,        int cardId,        String Name,        String phone,        String email    ) {
        this.adress = adress;
        this.cardId = cardId;
        this.Name = Name;
        this.phone = phone;
        this.email = email;
    }


    public String getAdress() {
        return adress;
    }

    public void setAdress(String adress) {
        this.adress = adress;
    }
    public int getCardid() {
        return cardId;
    }

    public void setCardid(int cardId) {
        this.cardId = cardId;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}