





import java.util.List;
import java.util.ArrayList;

public class Faculty  {

    private String ID;
    private String Username;
    private String Password;



    public Faculty(
        String ID,        String Username,        String Password    ) {
        this.ID = ID;
        this.Username = Username;
        this.Password = Password;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}