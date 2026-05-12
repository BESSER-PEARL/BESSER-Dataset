





import java.util.List;
import java.util.ArrayList;

public class WIS_Herde  {

    private String name;





    private Benutzer benutzer;




    private List<WIS_Weidegang> wis_weidegangs;


    public WIS_Herde(
        String name    ) {
        this.name = name;
        this.wis_weidegangs = new ArrayList<>();
    }

    public WIS_Herde(
        String name        ArrayList<WIS_Weidegang> wis_weidegangs    ) {
        this.name = name;
        this.wis_weidegangs = wis_weidegangs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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