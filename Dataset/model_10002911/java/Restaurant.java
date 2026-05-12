





import java.util.List;
import java.util.ArrayList;

public class Restaurant  {

    private None Menu;
    private String Name;
    private int PostCode;
    private String Address;



    public Restaurant(
        None Menu,        String Name,        int PostCode,        String Address    ) {
        this.Menu = Menu;
        this.Name = Name;
        this.PostCode = PostCode;
        this.Address = Address;
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
    public int getPostcode() {
        return PostCode;
    }

    public void setPostcode(int PostCode) {
        this.PostCode = PostCode;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}