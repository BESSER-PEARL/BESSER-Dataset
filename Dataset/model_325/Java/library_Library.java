





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String name;
    private int ages;
    private String address;



    public library_Library(
        String name,        int ages,        String address    ) {
        this.name = name;
        this.ages = ages;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAges() {
        return ages;
    }

    public void setAges(int ages) {
        this.ages = ages;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}