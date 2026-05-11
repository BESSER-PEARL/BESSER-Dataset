





import java.util.List;
import java.util.ArrayList;

public class dmm_Person  {

    private String email;
    private String name;





    private dmm_UniversityManagementSystem dmm_universitymanagementsystem;


    public dmm_Person(
        String email,        String name    ) {
        this.email = email;
        this.name = name;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dmm_UniversityManagementSystem getDmm_universitymanagementsystem() {
        return dmm_universitymanagementsystem;
    }

    public void setDmm_universitymanagementsystem(dmm_UniversityManagementSystem dmm_universitymanagementsystem) {
        this.dmm_universitymanagementsystem = dmm_universitymanagementsystem;
    }

}