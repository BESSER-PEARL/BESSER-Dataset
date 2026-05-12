





import java.util.List;
import java.util.ArrayList;

public class Rezervacija  {

    private int AgentID;
    private int RacunID;
    private None DatumKreiranja;
    private int PutnikID;
    private int ReyervacijaID;
    private int AranzmanID;



    public Rezervacija(
        int AgentID,        int RacunID,        None DatumKreiranja,        int PutnikID,        int ReyervacijaID,        int AranzmanID    ) {
        this.AgentID = AgentID;
        this.RacunID = RacunID;
        this.DatumKreiranja = DatumKreiranja;
        this.PutnikID = PutnikID;
        this.ReyervacijaID = ReyervacijaID;
        this.AranzmanID = AranzmanID;
    }


    public int getAgentid() {
        return AgentID;
    }

    public void setAgentid(int AgentID) {
        this.AgentID = AgentID;
    }
    public int getRacunid() {
        return RacunID;
    }

    public void setRacunid(int RacunID) {
        this.RacunID = RacunID;
    }
    public None getDatumkreiranja() {
        return DatumKreiranja;
    }

    public void setDatumkreiranja(None DatumKreiranja) {
        this.DatumKreiranja = DatumKreiranja;
    }
    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
    }
    public int getReyervacijaid() {
        return ReyervacijaID;
    }

    public void setReyervacijaid(int ReyervacijaID) {
        this.ReyervacijaID = ReyervacijaID;
    }
    public int getAranzmanid() {
        return AranzmanID;
    }

    public void setAranzmanid(int AranzmanID) {
        this.AranzmanID = AranzmanID;
    }


}