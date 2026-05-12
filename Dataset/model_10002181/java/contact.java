





import java.util.List;
import java.util.ArrayList;

public class contact  {

    private String Name;
    private String Email;
    private String attribute;
    private int Tel;
    private String Adress;





    private System1 system1;


    public contact(
        String Name,        String Email,        String attribute,        int Tel,        String Adress    ) {
        this.Name = Name;
        this.Email = Email;
        this.attribute = attribute;
        this.Tel = Tel;
        this.Adress = Adress;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getTel() {
        return Tel;
    }

    public void setTel(int Tel) {
        this.Tel = Tel;
    }
    public String getAdress() {
        return Adress;
    }

    public void setAdress(String Adress) {
        this.Adress = Adress;
    }

    public System1 getSystem1() {
        return system1;
    }

    public void setSystem1(System1 system1) {
        this.system1 = system1;
    }

}