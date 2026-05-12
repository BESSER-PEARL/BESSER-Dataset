





import java.util.List;
import java.util.ArrayList;

public class Presales_team  {

    private String password;
    private String usename;



    public Presales_team(
        String password,        String usename    ) {
        this.password = password;
        this.usename = usename;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsename() {
        return usename;
    }

    public void setUsename(String usename) {
        this.usename = usename;
    }


}