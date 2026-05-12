





import java.util.List;
import java.util.ArrayList;

public class Restaurant  {

    private None Menu;
    private int PostCode;
    private String Name;
    private String Address;



    public Restaurant(
        None Menu,        int PostCode,        String Name,        String Address    ) {
        this.Menu = Menu;
        this.PostCode = PostCode;
        this.Name = Name;
        this.Address = Address;
    }


    public None getMenu() {
        return Menu;
    }

    public void setMenu(None Menu) {
        this.Menu = Menu;
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
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}