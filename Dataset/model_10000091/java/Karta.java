





import java.util.List;
import java.util.ArrayList;

public class Karta  {

    private String CenaKarte;
    private String OdlazakKarta;
    private String VremeOdlaska;
    private int RezerID;
    private int KartaID;
    private String VremePovratka;
    private String PovratakKarta;



    public Karta(
        String CenaKarte,        String OdlazakKarta,        String VremeOdlaska,        int RezerID,        int KartaID,        String VremePovratka,        String PovratakKarta    ) {
        this.CenaKarte = CenaKarte;
        this.OdlazakKarta = OdlazakKarta;
        this.VremeOdlaska = VremeOdlaska;
        this.RezerID = RezerID;
        this.KartaID = KartaID;
        this.VremePovratka = VremePovratka;
        this.PovratakKarta = PovratakKarta;
    }


    public String getCenakarte() {
        return CenaKarte;
    }

    public void setCenakarte(String CenaKarte) {
        this.CenaKarte = CenaKarte;
    }
    public String getOdlazakkarta() {
        return OdlazakKarta;
    }

    public void setOdlazakkarta(String OdlazakKarta) {
        this.OdlazakKarta = OdlazakKarta;
    }
    public String getVremeodlaska() {
        return VremeOdlaska;
    }

    public void setVremeodlaska(String VremeOdlaska) {
        this.VremeOdlaska = VremeOdlaska;
    }
    public int getRezerid() {
        return RezerID;
    }

    public void setRezerid(int RezerID) {
        this.RezerID = RezerID;
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
    public String getPovratakkarta() {
        return PovratakKarta;
    }

    public void setPovratakkarta(String PovratakKarta) {
        this.PovratakKarta = PovratakKarta;
    }


}