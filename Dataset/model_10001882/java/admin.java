





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String name;
    private String mail;



    public Admin(
        String name,        String mail    ) {
        this.name = name;
        this.mail = mail;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }


}