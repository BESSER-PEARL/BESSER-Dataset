





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String attribute;
    private None Help__;
    private None Reverse__;
    private String adminName;
    private None Contact_Us__;
    private String email;



    public Admin(
        String attribute,        None Help__,        None Reverse__,        String adminName,        None Contact_Us__,        String email    ) {
        this.attribute = attribute;
        this.Help__ = Help__;
        this.Reverse__ = Reverse__;
        this.adminName = adminName;
        this.Contact_Us__ = Contact_Us__;
        this.email = email;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public None getHelp__() {
        return Help__;
    }

    public void setHelp__(None Help__) {
        this.Help__ = Help__;
    }
    public None getReverse__() {
        return Reverse__;
    }

    public void setReverse__(None Reverse__) {
        this.Reverse__ = Reverse__;
    }
    public String getAdminname() {
        return adminName;
    }

    public void setAdminname(String adminName) {
        this.adminName = adminName;
    }
    public None getContact_us__() {
        return Contact_Us__;
    }

    public void setContact_us__(None Contact_Us__) {
        this.Contact_Us__ = Contact_Us__;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}