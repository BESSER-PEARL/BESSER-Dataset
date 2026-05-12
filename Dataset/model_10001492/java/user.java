





import java.util.List;
import java.util.ArrayList;

public class user  {

    private String last_name;
    private String address;
    private int id;
    private int phone_number;
    private String first_name;
    private int card;
    private String email;



    public user(
        String last_name,        String address,        int id,        int phone_number,        String first_name,        int card,        String email    ) {
        this.last_name = last_name;
        this.address = address;
        this.id = id;
        this.phone_number = phone_number;
        this.first_name = first_name;
        this.card = card;
        this.email = email;
    }


    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPhone_number() {
        return phone_number;
    }

    public void setPhone_number(int phone_number) {
        this.phone_number = phone_number;
    }
    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public int getCard() {
        return card;
    }

    public void setCard(int card) {
        this.card = card;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}