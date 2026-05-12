





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String UslugaHotela;
    private int DuzinaBoravka;
    private int DestiID;
    private String CenaSmestaja;
    private int SobaHotela;
    private int SpratHotela;
    private String ImeHotela;
    private int HotelID;
    private String AdresaHotela;





    private Destinacija destinacija;


    public Hotel(
        String UslugaHotela,        int DuzinaBoravka,        int DestiID,        String CenaSmestaja,        int SobaHotela,        int SpratHotela,        String ImeHotela,        int HotelID,        String AdresaHotela    ) {
        this.UslugaHotela = UslugaHotela;
        this.DuzinaBoravka = DuzinaBoravka;
        this.DestiID = DestiID;
        this.CenaSmestaja = CenaSmestaja;
        this.SobaHotela = SobaHotela;
        this.SpratHotela = SpratHotela;
        this.ImeHotela = ImeHotela;
        this.HotelID = HotelID;
        this.AdresaHotela = AdresaHotela;
    }


    public String getUslugahotela() {
        return UslugaHotela;
    }

    public void setUslugahotela(String UslugaHotela) {
        this.UslugaHotela = UslugaHotela;
    }
    public int getDuzinaboravka() {
        return DuzinaBoravka;
    }

    public void setDuzinaboravka(int DuzinaBoravka) {
        this.DuzinaBoravka = DuzinaBoravka;
    }
    public int getDestiid() {
        return DestiID;
    }

    public void setDestiid(int DestiID) {
        this.DestiID = DestiID;
    }
    public String getCenasmestaja() {
        return CenaSmestaja;
    }

    public void setCenasmestaja(String CenaSmestaja) {
        this.CenaSmestaja = CenaSmestaja;
    }
    public int getSobahotela() {
        return SobaHotela;
    }

    public void setSobahotela(int SobaHotela) {
        this.SobaHotela = SobaHotela;
    }
    public int getSprathotela() {
        return SpratHotela;
    }

    public void setSprathotela(int SpratHotela) {
        this.SpratHotela = SpratHotela;
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

    public Destinacija getDestinacija() {
        return destinacija;
    }

    public void setDestinacija(Destinacija destinacija) {
        this.destinacija = destinacija;
    }

}