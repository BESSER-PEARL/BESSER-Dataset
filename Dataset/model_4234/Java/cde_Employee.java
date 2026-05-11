





import java.util.List;
import java.util.ArrayList;

public class cde_Employee  {

    private String address;
    private String name;



    public cde_Employee(
        String address,        String name    ) {
        this.address = address;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}