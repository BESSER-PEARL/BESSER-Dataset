





import java.util.List;
import java.util.ArrayList;

public class Karta  {

    private String OdlazakKarta;
    private int KartaID;
    private String VremeOdlaska;
    private String VremePovratka;
    private String PovratakKarta;
    private int RezerID;
    private String CenaKarte;



    public Karta(
        String OdlazakKarta,        int KartaID,        String VremeOdlaska,        String VremePovratka,        String PovratakKarta,        int RezerID,        String CenaKarte    ) {
        this.OdlazakKarta = OdlazakKarta;
        this.KartaID = KartaID;
        this.VremeOdlaska = VremeOdlaska;
        this.VremePovratka = VremePovratka;
        this.PovratakKarta = PovratakKarta;
        this.RezerID = RezerID;
        this.CenaKarte = CenaKarte;
    }


    public String getOdlazakkarta() {
        return OdlazakKarta;
    }

    public void setOdlazakkarta(String OdlazakKarta) {
        this.OdlazakKarta = OdlazakKarta;
    }
    public int getKartaid() {
        return KartaID;
    }

    public void setKartaid(int KartaID) {
        this.KartaID = KartaID;
    }
    public String getVremeodlaska() {
        return VremeOdlaska;
    }

    public void setVremeodlaska(String VremeOdlaska) {
        this.VremeOdlaska = VremeOdlaska;
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
    public int getRezerid() {
        return RezerID;
    }

    public void setRezerid(int RezerID) {
        this.RezerID = RezerID;
    }
    public String getCenakarte() {
        return CenaKarte;
    }

    public void setCenakarte(String CenaKarte) {
        this.CenaKarte = CenaKarte;
    }


}