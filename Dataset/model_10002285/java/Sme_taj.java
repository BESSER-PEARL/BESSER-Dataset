





import java.util.List;
import java.util.ArrayList;

public class Sme_taj  {

    private String LokacijaSme_taja;
    private String CenaSmestaja;
    private String ImeSme_taja;
    private String UslugaSme_taja;
    private int PutovID;
    private int Sme_tajID;
    private int DuzinaBoravka;





    private Putovanje putovanje;


    public Sme_taj(
        String LokacijaSme_taja,        String CenaSmestaja,        String ImeSme_taja,        String UslugaSme_taja,        int PutovID,        int Sme_tajID,        int DuzinaBoravka    ) {
        this.LokacijaSme_taja = LokacijaSme_taja;
        this.CenaSmestaja = CenaSmestaja;
        this.ImeSme_taja = ImeSme_taja;
        this.UslugaSme_taja = UslugaSme_taja;
        this.PutovID = PutovID;
        this.Sme_tajID = Sme_tajID;
        this.DuzinaBoravka = DuzinaBoravka;
    }


    public String getLokacijasme_taja() {
        return LokacijaSme_taja;
    }

    public void setLokacijasme_taja(String LokacijaSme_taja) {
        this.LokacijaSme_taja = LokacijaSme_taja;
    }
    public String getCenasmestaja() {
        return CenaSmestaja;
    }

    public void setCenasmestaja(String CenaSmestaja) {
        this.CenaSmestaja = CenaSmestaja;
    }
    public String getImesme_taja() {
        return ImeSme_taja;
    }

    public void setImesme_taja(String ImeSme_taja) {
        this.ImeSme_taja = ImeSme_taja;
    }
    public String getUslugasme_taja() {
        return UslugaSme_taja;
    }

    public void setUslugasme_taja(String UslugaSme_taja) {
        this.UslugaSme_taja = UslugaSme_taja;
    }
    public int getPutovid() {
        return PutovID;
    }

    public void setPutovid(int PutovID) {
        this.PutovID = PutovID;
    }
    public int getSme_tajid() {
        return Sme_tajID;
    }

    public void setSme_tajid(int Sme_tajID) {
        this.Sme_tajID = Sme_tajID;
    }
    public int getDuzinaboravka() {
        return DuzinaBoravka;
    }

    public void setDuzinaboravka(int DuzinaBoravka) {
        this.DuzinaBoravka = DuzinaBoravka;
    }

    public Putovanje getPutovanje() {
        return putovanje;
    }

    public void setPutovanje(Putovanje putovanje) {
        this.putovanje = putovanje;
    }

}