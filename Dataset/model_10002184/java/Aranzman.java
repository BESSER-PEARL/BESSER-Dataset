





import java.util.List;
import java.util.ArrayList;

public class Aranzman  {

    private String CenaAranzmana;
    private String OpisAranzmana;
    private int KorisnikID;
    private int VodicID;
    private String NazivAranzmana;
    private int AranzmanID;
    private String DatumAranzmana;
    private int HotelID;





    private Korisnik korisnik;




    private List<Putnik> putniks;


    public Aranzman(
        String CenaAranzmana,        String OpisAranzmana,        int KorisnikID,        int VodicID,        String NazivAranzmana,        int AranzmanID,        String DatumAranzmana,        int HotelID    ) {
        this.CenaAranzmana = CenaAranzmana;
        this.OpisAranzmana = OpisAranzmana;
        this.KorisnikID = KorisnikID;
        this.VodicID = VodicID;
        this.NazivAranzmana = NazivAranzmana;
        this.AranzmanID = AranzmanID;
        this.DatumAranzmana = DatumAranzmana;
        this.HotelID = HotelID;
        this.putniks = new ArrayList<>();
    }

    public Aranzman(
        String CenaAranzmana,        String OpisAranzmana,        int KorisnikID,        int VodicID,        String NazivAranzmana,        int AranzmanID,        String DatumAranzmana,        int HotelID        ArrayList<Putnik> putniks    ) {
        this.CenaAranzmana = CenaAranzmana;
        this.OpisAranzmana = OpisAranzmana;
        this.KorisnikID = KorisnikID;
        this.VodicID = VodicID;
        this.NazivAranzmana = NazivAranzmana;
        this.AranzmanID = AranzmanID;
        this.DatumAranzmana = DatumAranzmana;
        this.HotelID = HotelID;
        this.putniks = putniks;
    }

    public String getCenaaranzmana() {
        return CenaAranzmana;
    }

    public void setCenaaranzmana(String CenaAranzmana) {
        this.CenaAranzmana = CenaAranzmana;
    }
    public String getOpisaranzmana() {
        return OpisAranzmana;
    }

    public void setOpisaranzmana(String OpisAranzmana) {
        this.OpisAranzmana = OpisAranzmana;
    }
    public int getKorisnikid() {
        return KorisnikID;
    }

    public void setKorisnikid(int KorisnikID) {
        this.KorisnikID = KorisnikID;
    }
    public int getVodicid() {
        return VodicID;
    }

    public void setVodicid(int VodicID) {
        this.VodicID = VodicID;
    }
    public String getNazivaranzmana() {
        return NazivAranzmana;
    }

    public void setNazivaranzmana(String NazivAranzmana) {
        this.NazivAranzmana = NazivAranzmana;
    }
    public int getAranzmanid() {
        return AranzmanID;
    }

    public void setAranzmanid(int AranzmanID) {
        this.AranzmanID = AranzmanID;
    }
    public String getDatumaranzmana() {
        return DatumAranzmana;
    }

    public void setDatumaranzmana(String DatumAranzmana) {
        this.DatumAranzmana = DatumAranzmana;
    }
    public int getHotelid() {
        return HotelID;
    }

    public void setHotelid(int HotelID) {
        this.HotelID = HotelID;
    }

    public Korisnik getKorisnik() {
        return korisnik;
    }

    public void setKorisnik(Korisnik korisnik) {
        this.korisnik = korisnik;
    }
    public List<Putnik> getPutniks() {
        return putniks;
    }

    public void addPutnik(Putnik putnik) {
        this.putniks.add(putnik);
    }

}