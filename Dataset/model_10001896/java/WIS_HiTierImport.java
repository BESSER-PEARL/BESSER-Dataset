





import java.util.List;
import java.util.ArrayList;

public class WIS_HiTierImport  {

    private String datum;





    private List<WIS_Tier> wis_tiers;




    private Benutzer benutzer;


    public WIS_HiTierImport(
        String datum    ) {
        this.datum = datum;
        this.wis_tiers = new ArrayList<>();
    }

    public WIS_HiTierImport(
        String datum        ArrayList<WIS_Tier> wis_tiers    ) {
        this.datum = datum;
        this.wis_tiers = wis_tiers;
    }

    public String getDatum() {
        return datum;
    }

    public void setDatum(String datum) {
        this.datum = datum;
    }

    public List<WIS_Tier> getWis_tiers() {
        return wis_tiers;
    }

    public void addWis_tier(Wis_tier wis_tier) {
        this.wis_tiers.add(wis_tier);
    }
    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }

}