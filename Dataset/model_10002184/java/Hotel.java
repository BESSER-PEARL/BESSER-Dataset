





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String AdresaHotela;
    private int GradID;
    private String KontaktHotela;
    private int HotelID;
    private String NazivHotela;





    private List<Aranzman> aranzmans;


    public Hotel(
        String AdresaHotela,        int GradID,        String KontaktHotela,        int HotelID,        String NazivHotela    ) {
        this.AdresaHotela = AdresaHotela;
        this.GradID = GradID;
        this.KontaktHotela = KontaktHotela;
        this.HotelID = HotelID;
        this.NazivHotela = NazivHotela;
        this.aranzmans = new ArrayList<>();
    }

    public Hotel(
        String AdresaHotela,        int GradID,        String KontaktHotela,        int HotelID,        String NazivHotela        ArrayList<Aranzman> aranzmans    ) {
        this.AdresaHotela = AdresaHotela;
        this.GradID = GradID;
        this.KontaktHotela = KontaktHotela;
        this.HotelID = HotelID;
        this.NazivHotela = NazivHotela;
        this.aranzmans = aranzmans;
    }

    public String getAdresahotela() {
        return AdresaHotela;
    }

    public void setAdresahotela(String AdresaHotela) {
        this.AdresaHotela = AdresaHotela;
    }
    public int getGradid() {
        return GradID;
    }

    public void setGradid(int GradID) {
        this.GradID = GradID;
    }
    public String getKontakthotela() {
        return KontaktHotela;
    }

    public void setKontakthotela(String KontaktHotela) {
        this.KontaktHotela = KontaktHotela;
    }
    public int getHotelid() {
        return HotelID;
    }

    public void setHotelid(int HotelID) {
        this.HotelID = HotelID;
    }
    public String getNazivhotela() {
        return NazivHotela;
    }

    public void setNazivhotela(String NazivHotela) {
        this.NazivHotela = NazivHotela;
    }

    public List<Aranzman> getAranzmans() {
        return aranzmans;
    }

    public void addAranzman(Aranzman aranzman) {
        this.aranzmans.add(aranzman);
    }

}