





import java.util.List;
import java.util.ArrayList;

public class Benutzer  {

    private String passwortHash;
    private String name;



    public Benutzer(
        String passwortHash,        String name    ) {
        this.passwortHash = passwortHash;
        this.name = name;
    }


    public String getPassworthash() {
        return passwortHash;
    }

    public void setPassworthash(String passwortHash) {
        this.passwortHash = passwortHash;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}