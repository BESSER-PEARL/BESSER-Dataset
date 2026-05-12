





import java.util.List;
import java.util.ArrayList;

public class Karta  {

    private String CenaKarte;
    private String VremeOdlaska;
    private String OdlazakKarta;
    private int RezerID;
    private String PovratakKarta;
    private int KartaID;
    private String VremePovratka;



    public Karta(
        String CenaKarte,        String VremeOdlaska,        String OdlazakKarta,        int RezerID,        String PovratakKarta,        int KartaID,        String VremePovratka    ) {
        this.CenaKarte = CenaKarte;
        this.VremeOdlaska = VremeOdlaska;
        this.OdlazakKarta = OdlazakKarta;
        this.RezerID = RezerID;
        this.PovratakKarta = PovratakKarta;
        this.KartaID = KartaID;
        this.VremePovratka = VremePovratka;
    }


    public String getCenakarte() {
        return CenaKarte;
    }

    public void setCenakarte(String CenaKarte) {
        this.CenaKarte = CenaKarte;
    }
    public String getVremeodlaska() {
        return VremeOdlaska;
    }

    public void setVremeodlaska(String VremeOdlaska) {
        this.VremeOdlaska = VremeOdlaska;
    }
    public String getOdlazakkarta() {
        return OdlazakKarta;
    }

    public void setOdlazakkarta(String OdlazakKarta) {
        this.OdlazakKarta = OdlazakKarta;
    }
    public int getRezerid() {
        return RezerID;
    }

    public void setRezerid(int RezerID) {
        this.RezerID = RezerID;
    }
    public String getPovratakkarta() {
        return PovratakKarta;
    }

    public void setPovratakkarta(String PovratakKarta) {
        this.PovratakKarta = PovratakKarta;
    }
    public int getKartaid() {
        return KartaID;
    }

    public void setKartaid(int KartaID) {
        this.KartaID = KartaID;
    }
    public String getVremepovratka() {
        return VremePovratka;
    }

    public void setVremepovratka(String VremePovratka) {
        this.VremePovratka = VremePovratka;
    }


}