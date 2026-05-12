





import java.util.List;
import java.util.ArrayList;

public class User1  {

    private String campus;
    private String attribute;
    private String name;
    private boolean isStaff;
    private String email;
    private String username;





    private VirtualTour1 virtualtour1;


    public User1(
        String campus,        String attribute,        String name,        boolean isStaff,        String email,        String username    ) {
        this.campus = campus;
        this.attribute = attribute;
        this.name = name;
        this.isStaff = isStaff;
        this.email = email;
        this.username = username;
    }


    public String getCampus() {
        return campus;
    }

    public void setCampus(String campus) {
        this.campus = campus;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsstaff() {
        return isStaff;
    }

    public void setIsstaff(boolean isStaff) {
        this.isStaff = isStaff;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public VirtualTour1 getVirtualtour1() {
        return virtualtour1;
    }

    public void setVirtualtour1(VirtualTour1 virtualtour1) {
        this.virtualtour1 = virtualtour1;
    }

}