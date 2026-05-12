





import java.util.List;
import java.util.ArrayList;

public class Aran_man  {

    private String Cena;
    private boolean SlobMesto;
    private String DatumPovratka;
    private String Aranzman_ID;
    private String DatumPolaska;
    private String NazivAran_;





    private List<Agent> agents;


    public Aran_man(
        String Cena,        boolean SlobMesto,        String DatumPovratka,        String Aranzman_ID,        String DatumPolaska,        String NazivAran_    ) {
        this.Cena = Cena;
        this.SlobMesto = SlobMesto;
        this.DatumPovratka = DatumPovratka;
        this.Aranzman_ID = Aranzman_ID;
        this.DatumPolaska = DatumPolaska;
        this.NazivAran_ = NazivAran_;
        this.agents = new ArrayList<>();
    }

    public Aran_man(
        String Cena,        boolean SlobMesto,        String DatumPovratka,        String Aranzman_ID,        String DatumPolaska,        String NazivAran_        ArrayList<Agent> agents    ) {
        this.Cena = Cena;
        this.SlobMesto = SlobMesto;
        this.DatumPovratka = DatumPovratka;
        this.Aranzman_ID = Aranzman_ID;
        this.DatumPolaska = DatumPolaska;
        this.NazivAran_ = NazivAran_;
        this.agents = agents;
    }

    public String getCena() {
        return Cena;
    }

    public void setCena(String Cena) {
        this.Cena = Cena;
    }
    public boolean getSlobmesto() {
        return SlobMesto;
    }

    public void setSlobmesto(boolean SlobMesto) {
        this.SlobMesto = SlobMesto;
    }
    public String getDatumpovratka() {
        return DatumPovratka;
    }

    public void setDatumpovratka(String DatumPovratka) {
        this.DatumPovratka = DatumPovratka;
    }
    public String getAranzman_id() {
        return Aranzman_ID;
    }

    public void setAranzman_id(String Aranzman_ID) {
        this.Aranzman_ID = Aranzman_ID;
    }
    public String getDatumpolaska() {
        return DatumPolaska;
    }

    public void setDatumpolaska(String DatumPolaska) {
        this.DatumPolaska = DatumPolaska;
    }
    public String getNazivaran_() {
        return NazivAran_;
    }

    public void setNazivaran_(String NazivAran_) {
        this.NazivAran_ = NazivAran_;
    }

    public List<Agent> getAgents() {
        return agents;
    }

    public void addAgent(Agent agent) {
        this.agents.add(agent);
    }

}