





import java.util.List;
import java.util.ArrayList;

public class Vodic  {

    private String AdresaVodica;
    private String PrezimeVodica;
    private int VodicID;
    private String GradVodica;
    private String JMBG;
    private String ImeVodica;
    private String KontaktVodica;





    private List<Aranzman> aranzmans;


    public Vodic(
        String AdresaVodica,        String PrezimeVodica,        int VodicID,        String GradVodica,        String JMBG,        String ImeVodica,        String KontaktVodica    ) {
        this.AdresaVodica = AdresaVodica;
        this.PrezimeVodica = PrezimeVodica;
        this.VodicID = VodicID;
        this.GradVodica = GradVodica;
        this.JMBG = JMBG;
        this.ImeVodica = ImeVodica;
        this.KontaktVodica = KontaktVodica;
        this.aranzmans = new ArrayList<>();
    }

    public Vodic(
        String AdresaVodica,        String PrezimeVodica,        int VodicID,        String GradVodica,        String JMBG,        String ImeVodica,        String KontaktVodica        ArrayList<Aranzman> aranzmans    ) {
        this.AdresaVodica = AdresaVodica;
        this.PrezimeVodica = PrezimeVodica;
        this.VodicID = VodicID;
        this.GradVodica = GradVodica;
        this.JMBG = JMBG;
        this.ImeVodica = ImeVodica;
        this.KontaktVodica = KontaktVodica;
        this.aranzmans = aranzmans;
    }

    public String getAdresavodica() {
        return AdresaVodica;
    }

    public void setAdresavodica(String AdresaVodica) {
        this.AdresaVodica = AdresaVodica;
    }
    public String getPrezimevodica() {
        return PrezimeVodica;
    }

    public void setPrezimevodica(String PrezimeVodica) {
        this.PrezimeVodica = PrezimeVodica;
    }
    public int getVodicid() {
        return VodicID;
    }

    public void setVodicid(int VodicID) {
        this.VodicID = VodicID;
    }
    public String getGradvodica() {
        return GradVodica;
    }

    public void setGradvodica(String GradVodica) {
        this.GradVodica = GradVodica;
    }
    public String getJmbg() {
        return JMBG;
    }

    public void setJmbg(String JMBG) {
        this.JMBG = JMBG;
    }
    public String getImevodica() {
        return ImeVodica;
    }

    public void setImevodica(String ImeVodica) {
        this.ImeVodica = ImeVodica;
    }
    public String getKontaktvodica() {
        return KontaktVodica;
    }

    public void setKontaktvodica(String KontaktVodica) {
        this.KontaktVodica = KontaktVodica;
    }

    public List<Aranzman> getAranzmans() {
        return aranzmans;
    }

    public void addAranzman(Aranzman aranzman) {
        this.aranzmans.add(aranzman);
    }

}