





import java.util.List;
import java.util.ArrayList;

public class javaMM_ManifestEntry  {

    private String name;





    private List<javaMM_ManifestAttribute> javamm_manifestattributes;


    public javaMM_ManifestEntry(
        String name    ) {
        this.name = name;
        this.javamm_manifestattributes = new ArrayList<>();
    }

    public javaMM_ManifestEntry(
        String name        ArrayList<javaMM_ManifestAttribute> javamm_manifestattributes    ) {
        this.name = name;
        this.javamm_manifestattributes = javamm_manifestattributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<javaMM_ManifestAttribute> getJavamm_manifestattributes() {
        return javamm_manifestattributes;
    }

    public void addJavamm_manifestattribute(Javamm_manifestattribute javamm_manifestattribute) {
        this.javamm_manifestattributes.add(javamm_manifestattribute);
    }

}