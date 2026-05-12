





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String address;
    private String qualification;
    private String name;



    public Admin(
        String address,        String qualification,        String name    ) {
        this.address = address;
        this.qualification = qualification;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getQualification() {
        return qualification;
    }

    public void setQualification(String qualification) {
        this.qualification = qualification;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}