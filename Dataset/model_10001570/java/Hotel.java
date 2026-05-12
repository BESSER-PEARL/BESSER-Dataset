





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String UslugaHotela;
    private int SobaHotela;
    private int DestiID;
    private int SpratHotela;
    private int DuzinaBoravka;
    private String ImeHotela;
    private int HotelID;
    private String AdresaHotela;
    private String CenaSmestaja;





    private Destinacija destinacija;


    public Hotel(
        String UslugaHotela,        int SobaHotela,        int DestiID,        int SpratHotela,        int DuzinaBoravka,        String ImeHotela,        int HotelID,        String AdresaHotela,        String CenaSmestaja    ) {
        this.UslugaHotela = UslugaHotela;
        this.SobaHotela = SobaHotela;
        this.DestiID = DestiID;
        this.SpratHotela = SpratHotela;
        this.DuzinaBoravka = DuzinaBoravka;
        this.ImeHotela = ImeHotela;
        this.HotelID = HotelID;
        this.AdresaHotela = AdresaHotela;
        this.CenaSmestaja = CenaSmestaja;
    }


    public String getUslugahotela() {
        return UslugaHotela;
    }

    public void setUslugahotela(String UslugaHotela) {
        this.UslugaHotela = UslugaHotela;
    }
    public int getSobahotela() {
        return SobaHotela;
    }

    public void setSobahotela(int SobaHotela) {
        this.SobaHotela = SobaHotela;
    }
    public int getDestiid() {
        return DestiID;
    }

    public void setDestiid(int DestiID) {
        this.DestiID = DestiID;
    }
    public int getSprathotela() {
        return SpratHotela;
    }

    public void setSprathotela(int SpratHotela) {
        this.SpratHotela = SpratHotela;
    }
    public int getDuzinaboravka() {
        return DuzinaBoravka;
    }

    public void setDuzinaboravka(int DuzinaBoravka) {
        this.DuzinaBoravka = DuzinaBoravka;
    }
    public String getImehotela() {
        return ImeHotela;
    }

    public void setImehotela(String ImeHotela) {
        this.ImeHotela = ImeHotela;
    }
    public int getHotelid() {
        return HotelID;
    }

    public void setHotelid(int HotelID) {
        this.HotelID = HotelID;
    }
    public String getAdresahotela() {
        return AdresaHotela;
    }

    public void setAdresahotela(String AdresaHotela) {
        this.AdresaHotela = AdresaHotela;
    }
    public String getCenasmestaja() {
        return CenaSmestaja;
    }

    public void setCenasmestaja(String CenaSmestaja) {
        this.CenaSmestaja = CenaSmestaja;
    }

    public Destinacija getDestinacija() {
        return destinacija;
    }

    public void setDestinacija(Destinacija destinacija) {
        this.destinacija = destinacija;
    }

}