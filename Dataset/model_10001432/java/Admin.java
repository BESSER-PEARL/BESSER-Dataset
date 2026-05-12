





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String Password;
    private String Username;





    private Pemilik pemilik;


    public Admin(
        String Password,        String Username    ) {
        this.Password = Password;
        this.Username = Username;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }

    public Pemilik getPemilik() {
        return pemilik;
    }

    public void setPemilik(Pemilik pemilik) {
        this.pemilik = pemilik;
    }

}