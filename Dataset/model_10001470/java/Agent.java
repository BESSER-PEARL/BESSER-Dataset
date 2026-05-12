





import java.util.List;
import java.util.ArrayList;

public class Agent  {

    private String PrezimeAgent;
    private String Username;
    private String Email;
    private String Password;
    private String BrojTele;
    private String ImeAgent;
    private int AgentID;





    private Rezervacija rezervacija;


    public Agent(
        String PrezimeAgent,        String Username,        String Email,        String Password,        String BrojTele,        String ImeAgent,        int AgentID    ) {
        this.PrezimeAgent = PrezimeAgent;
        this.Username = Username;
        this.Email = Email;
        this.Password = Password;
        this.BrojTele = BrojTele;
        this.ImeAgent = ImeAgent;
        this.AgentID = AgentID;
    }


    public String getPrezimeagent() {
        return PrezimeAgent;
    }

    public void setPrezimeagent(String PrezimeAgent) {
        this.PrezimeAgent = PrezimeAgent;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getBrojtele() {
        return BrojTele;
    }

    public void setBrojtele(String BrojTele) {
        this.BrojTele = BrojTele;
    }
    public String getImeagent() {
        return ImeAgent;
    }

    public void setImeagent(String ImeAgent) {
        this.ImeAgent = ImeAgent;
    }
    public int getAgentid() {
        return AgentID;
    }

    public void setAgentid(int AgentID) {
        this.AgentID = AgentID;
    }

    public Rezervacija getRezervacija() {
        return rezervacija;
    }

    public void setRezervacija(Rezervacija rezervacija) {
        this.rezervacija = rezervacija;
    }

}