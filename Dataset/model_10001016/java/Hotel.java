





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String CenaSmestaja;
    private String UslugaHotela;
    private int HotelID;
    private String ImeHotela;
    private int SobaHotela;
    private String AdresaHotela;
    private int DuzinaBoravka;
    private int DestiID;
    private int SpratHotela;





    private Destinacija destinacija;


    public Hotel(
        String CenaSmestaja,        String UslugaHotela,        int HotelID,        String ImeHotela,        int SobaHotela,        String AdresaHotela,        int DuzinaBoravka,        int DestiID,        int SpratHotela    ) {
        this.CenaSmestaja = CenaSmestaja;
        this.UslugaHotela = UslugaHotela;
        this.HotelID = HotelID;
        this.ImeHotela = ImeHotela;
        this.SobaHotela = SobaHotela;
        this.AdresaHotela = AdresaHotela;
        this.DuzinaBoravka = DuzinaBoravka;
        this.DestiID = DestiID;
        this.SpratHotela = SpratHotela;
    }


    public String getCenasmestaja() {
        return CenaSmestaja;
    }

    public void setCenasmestaja(String CenaSmestaja) {
        this.CenaSmestaja = CenaSmestaja;
    }
    public String getUslugahotela() {
        return UslugaHotela;
    }

    public void setUslugahotela(String UslugaHotela) {
        this.UslugaHotela = UslugaHotela;
    }
    public int getHotelid() {
        return HotelID;
    }

    public void setHotelid(int HotelID) {
        this.HotelID = HotelID;
    }
    public String getImehotela() {
        return ImeHotela;
    }

    public void setImehotela(String ImeHotela) {
        this.ImeHotela = ImeHotela;
    }
    public int getSobahotela() {
        return SobaHotela;
    }

    public void setSobahotela(int SobaHotela) {
        this.SobaHotela = SobaHotela;
    }
    public String getAdresahotela() {
        return AdresaHotela;
    }

    public void setAdresahotela(String AdresaHotela) {
        this.AdresaHotela = AdresaHotela;
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
    public int getSprathotela() {
        return SpratHotela;
    }

    public void setSprathotela(int SpratHotela) {
        this.SpratHotela = SpratHotela;
    }

    public Destinacija getDestinacija() {
        return destinacija;
    }

    public void setDestinacija(Destinacija destinacija) {
        this.destinacija = destinacija;
    }

}