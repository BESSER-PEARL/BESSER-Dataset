





import java.util.List;
import java.util.ArrayList;

public class WIS_Tier  {

    private String eigeneAngaben;
    private String transponderNummer;
    private String geburtsdatum;
    private boolean istAktiv;
    private String BTV8;
    private String BTV4;
    private String letzteKalbung;
    private boolean istWeiblich;
    private String name;
    private String UDNummer;
    private int LOM;





    private WIS_Herde wis_herde;




    private Benutzer benutzer;




    private List<WIS_Weidegang> wis_weidegangs;


    public WIS_Tier(
        String eigeneAngaben,        String transponderNummer,        String geburtsdatum,        boolean istAktiv,        String BTV8,        String BTV4,        String letzteKalbung,        boolean istWeiblich,        String name,        String UDNummer,        int LOM    ) {
        this.eigeneAngaben = eigeneAngaben;
        this.transponderNummer = transponderNummer;
        this.geburtsdatum = geburtsdatum;
        this.istAktiv = istAktiv;
        this.BTV8 = BTV8;
        this.BTV4 = BTV4;
        this.letzteKalbung = letzteKalbung;
        this.istWeiblich = istWeiblich;
        this.name = name;
        this.UDNummer = UDNummer;
        this.LOM = LOM;
        this.wis_weidegangs = new ArrayList<>();
    }

    public WIS_Tier(
        String eigeneAngaben,        String transponderNummer,        String geburtsdatum,        boolean istAktiv,        String BTV8,        String BTV4,        String letzteKalbung,        boolean istWeiblich,        String name,        String UDNummer,        int LOM        ArrayList<WIS_Weidegang> wis_weidegangs    ) {
        this.eigeneAngaben = eigeneAngaben;
        this.transponderNummer = transponderNummer;
        this.geburtsdatum = geburtsdatum;
        this.istAktiv = istAktiv;
        this.BTV8 = BTV8;
        this.BTV4 = BTV4;
        this.letzteKalbung = letzteKalbung;
        this.istWeiblich = istWeiblich;
        this.name = name;
        this.UDNummer = UDNummer;
        this.LOM = LOM;
        this.wis_weidegangs = wis_weidegangs;
    }

    public String getEigeneangaben() {
        return eigeneAngaben;
    }

    public void setEigeneangaben(String eigeneAngaben) {
        this.eigeneAngaben = eigeneAngaben;
    }
    public String getTranspondernummer() {
        return transponderNummer;
    }

    public void setTranspondernummer(String transponderNummer) {
        this.transponderNummer = transponderNummer;
    }
    public String getGeburtsdatum() {
        return geburtsdatum;
    }

    public void setGeburtsdatum(String geburtsdatum) {
        this.geburtsdatum = geburtsdatum;
    }
    public boolean getIstaktiv() {
        return istAktiv;
    }

    public void setIstaktiv(boolean istAktiv) {
        this.istAktiv = istAktiv;
    }
    public String getBtv8() {
        return BTV8;
    }

    public void setBtv8(String BTV8) {
        this.BTV8 = BTV8;
    }
    public String getBtv4() {
        return BTV4;
    }

    public void setBtv4(String BTV4) {
        this.BTV4 = BTV4;
    }
    public String getLetztekalbung() {
        return letzteKalbung;
    }

    public void setLetztekalbung(String letzteKalbung) {
        this.letzteKalbung = letzteKalbung;
    }
    public boolean getIstweiblich() {
        return istWeiblich;
    }

    public void setIstweiblich(boolean istWeiblich) {
        this.istWeiblich = istWeiblich;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUdnummer() {
        return UDNummer;
    }

    public void setUdnummer(String UDNummer) {
        this.UDNummer = UDNummer;
    }
    public int getLom() {
        return LOM;
    }

    public void setLom(int LOM) {
        this.LOM = LOM;
    }

    public WIS_Herde getWis_herde() {
        return wis_herde;
    }

    public void setWis_herde(WIS_Herde wis_herde) {
        this.wis_herde = wis_herde;
    }
    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }
    public List<WIS_Weidegang> getWis_weidegangs() {
        return wis_weidegangs;
    }

    public void addWis_weidegang(Wis_weidegang wis_weidegang) {
        this.wis_weidegangs.add(wis_weidegang);
    }

}