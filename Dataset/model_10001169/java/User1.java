





import java.util.List;
import java.util.ArrayList;

public class User1  {

    private String campus;
    private String email;
    private String attribute;
    private String username;
    private String name;
    private boolean isStaff;





    private VirtualTour1 virtualtour1;


    public User1(
        String campus,        String email,        String attribute,        String username,        String name,        boolean isStaff    ) {
        this.campus = campus;
        this.email = email;
        this.attribute = attribute;
        this.username = username;
        this.name = name;
        this.isStaff = isStaff;
    }


    public String getCampus() {
        return campus;
    }

    public void setCampus(String campus) {
        this.campus = campus;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
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

    public VirtualTour1 getVirtualtour1() {
        return virtualtour1;
    }

    public void setVirtualtour1(VirtualTour1 virtualtour1) {
        this.virtualtour1 = virtualtour1;
    }

}