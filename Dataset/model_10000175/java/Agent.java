





import java.util.List;
import java.util.ArrayList;

public class Agent  {

    private String Agent_ID;
    private String Ime;
    private int BrojAgenta;
    private String Prezime;
    private int JMBG;



    public Agent(
        String Agent_ID,        String Ime,        int BrojAgenta,        String Prezime,        int JMBG    ) {
        this.Agent_ID = Agent_ID;
        this.Ime = Ime;
        this.BrojAgenta = BrojAgenta;
        this.Prezime = Prezime;
        this.JMBG = JMBG;
    }


    public String getAgent_id() {
        return Agent_ID;
    }

    public void setAgent_id(String Agent_ID) {
        this.Agent_ID = Agent_ID;
    }
    public String getIme() {
        return Ime;
    }

    public void setIme(String Ime) {
        this.Ime = Ime;
    }
    public int getBrojagenta() {
        return BrojAgenta;
    }

    public void setBrojagenta(int BrojAgenta) {
        this.BrojAgenta = BrojAgenta;
    }
    public String getPrezime() {
        return Prezime;
    }

    public void setPrezime(String Prezime) {
        this.Prezime = Prezime;
    }
    public int getJmbg() {
        return JMBG;
    }

    public void setJmbg(int JMBG) {
        this.JMBG = JMBG;
    }


}