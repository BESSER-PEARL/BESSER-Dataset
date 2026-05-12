





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String qualification;
    private String name;
    private String address;



    public Admin(
        String qualification,        String name,        String address    ) {
        this.qualification = qualification;
        this.name = name;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}