





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Publisher  {

    private String name;
    private String address;



    public sistedesMM_Publisher(
        String name,        String address    ) {
        this.name = name;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}