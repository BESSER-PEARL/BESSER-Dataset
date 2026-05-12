





import java.util.List;
import java.util.ArrayList;

public class Termin  {

    private int TerminID;
    private None DatumPovratka;
    private None DatumPolaska;





    private Aranzman aranzman;


    public Termin(
        int TerminID,        None DatumPovratka,        None DatumPolaska    ) {
        this.TerminID = TerminID;
        this.DatumPovratka = DatumPovratka;
        this.DatumPolaska = DatumPolaska;
    }


    public int getTerminid() {
        return TerminID;
    }

    public void setTerminid(int TerminID) {
        this.TerminID = TerminID;
    }
    public None getDatumpovratka() {
        return DatumPovratka;
    }

    public void setDatumpovratka(None DatumPovratka) {
        this.DatumPovratka = DatumPovratka;
    }
    public None getDatumpolaska() {
        return DatumPolaska;
    }

    public void setDatumpolaska(None DatumPolaska) {
        this.DatumPolaska = DatumPolaska;
    }

    public Aranzman getAranzman() {
        return aranzman;
    }

    public void setAranzman(Aranzman aranzman) {
        this.aranzman = aranzman;
    }

}