





import java.util.List;
import java.util.ArrayList;

public class Restaurant  {

    private int PostCode;
    private String Name;
    private None Menu;
    private String Address;



    public Restaurant(
        int PostCode,        String Name,        None Menu,        String Address    ) {
        this.PostCode = PostCode;
        this.Name = Name;
        this.Menu = Menu;
        this.Address = Address;
    }


    public int getPostcode() {
        return PostCode;
    }

    public void setPostcode(int PostCode) {
        this.PostCode = PostCode;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public None getMenu() {
        return Menu;
    }

    public void setMenu(None Menu) {
        this.Menu = Menu;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}