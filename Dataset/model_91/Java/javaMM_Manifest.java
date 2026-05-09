





import java.util.List;
import java.util.ArrayList;

public class javaMM_Manifest  {






    private List<javaMM_ManifestAttribute> javamm_manifestattributes;




    private List<javaMM_ManifestEntry> javamm_manifestentrys;


    public javaMM_Manifest(
    ) {
        this.javamm_manifestattributes = new ArrayList<>();
        this.javamm_manifestentrys = new ArrayList<>();
    }

    public javaMM_Manifest(
        ArrayList<javaMM_ManifestAttribute> javamm_manifestattributes,        ArrayList<javaMM_ManifestEntry> javamm_manifestentrys    ) {
        this.javamm_manifestattributes = javamm_manifestattributes;
        this.javamm_manifestentrys = javamm_manifestentrys;
    }


    public List<javaMM_ManifestAttribute> getJavamm_manifestattributes() {
        return javamm_manifestattributes;
    }

    public void addJavamm_manifestattribute(Javamm_manifestattribute javamm_manifestattribute) {
        this.javamm_manifestattributes.add(javamm_manifestattribute);
    }
    public List<javaMM_ManifestEntry> getJavamm_manifestentrys() {
        return javamm_manifestentrys;
    }

    public void addJavamm_manifestentry(Javamm_manifestentry javamm_manifestentry) {
        this.javamm_manifestentrys.add(javamm_manifestentry);
    }

}