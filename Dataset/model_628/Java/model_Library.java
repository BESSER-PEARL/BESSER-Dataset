





import java.util.List;
import java.util.ArrayList;

public class model_Library  {

    private String name;
    private String phoneNumber;



    public model_Library(
        String name,        String phoneNumber    ) {
        this.name = name;
        this.phoneNumber = phoneNumber;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }


}