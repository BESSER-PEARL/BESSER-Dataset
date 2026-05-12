





import java.util.List;
import java.util.ArrayList;

public class Owner  {

    private String email;
    private String items;



    public Owner(
        String email,        String items    ) {
        this.email = email;
        this.items = items;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }


}