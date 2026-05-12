





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FilterSet extends Set {

    private String endtoken;
    private String starttoken;





    private List<MavenMaven_FiltersFile> mavenmaven_filtersfiles;


    public MavenMaven_FilterSet(
        String endtoken,        String starttoken    ) {
        super(
        );
        this.endtoken = endtoken;
        this.starttoken = starttoken;
        this.mavenmaven_filtersfiles = new ArrayList<>();
    }

    public MavenMaven_FilterSet(
        String endtoken,        String starttoken        ArrayList<MavenMaven_FiltersFile> mavenmaven_filtersfiles    ) {
        this.endtoken = endtoken;
        this.starttoken = starttoken;
        this.mavenmaven_filtersfiles = mavenmaven_filtersfiles;
    }

    public String getEndtoken() {
        return endtoken;
    }

    public void setEndtoken(String endtoken) {
        this.endtoken = endtoken;
    }
    public String getStarttoken() {
        return starttoken;
    }

    public void setStarttoken(String starttoken) {
        this.starttoken = starttoken;
    }

    public List<MavenMaven_FiltersFile> getMavenmaven_filtersfiles() {
        return mavenmaven_filtersfiles;
    }

    public void addMavenmaven_filtersfile(Mavenmaven_filtersfile mavenmaven_filtersfile) {
        this.mavenmaven_filtersfiles.add(mavenmaven_filtersfile);
    }

}