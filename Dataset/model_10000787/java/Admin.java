





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String address;
    private int name;



    public Admin(
        String address,        int name    ) {
        this.address = address;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }


}