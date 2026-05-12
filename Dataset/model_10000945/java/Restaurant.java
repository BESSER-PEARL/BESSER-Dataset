





import java.util.List;
import java.util.ArrayList;

public class Restaurant  {

    private int PostCode;
    private None Menu;
    private String Name;
    private String Address;



    public Restaurant(
        int PostCode,        None Menu,        String Name,        String Address    ) {
        this.PostCode = PostCode;
        this.Menu = Menu;
        this.Name = Name;
        this.Address = Address;
    }


    public int getPostcode() {
        return PostCode;
    }

    public void setPostcode(int PostCode) {
        this.PostCode = PostCode;
    }
    public None getMenu() {
        return Menu;
    }

    public void setMenu(None Menu) {
        this.Menu = Menu;
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