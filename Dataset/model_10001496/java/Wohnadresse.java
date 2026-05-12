





import java.util.List;
import java.util.ArrayList;

public class Wohnadresse  {

    private String Strasse;
    private int PLZ;
    private String Land;
    private String Stadt;





    private Person person;


    public Wohnadresse(
        String Strasse,        int PLZ,        String Land,        String Stadt    ) {
        this.Strasse = Strasse;
        this.PLZ = PLZ;
        this.Land = Land;
        this.Stadt = Stadt;
    }


    public String getStrasse() {
        return Strasse;
    }

    public void setStrasse(String Strasse) {
        this.Strasse = Strasse;
    }
    public int getPlz() {
        return PLZ;
    }

    public void setPlz(int PLZ) {
        this.PLZ = PLZ;
    }
    public String getLand() {
        return Land;
    }

    public void setLand(String Land) {
        this.Land = Land;
    }
    public String getStadt() {
        return Stadt;
    }

    public void setStadt(String Stadt) {
        this.Stadt = Stadt;
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}