





import java.util.List;
import java.util.ArrayList;

public class trackit_Product extends Identifiable {

    private String name;





    private List<trackit_Version> trackit_versions;




    private trackit_IssueTracker trackit_issuetracker;




    private trackit_Version trackit_version;


    public trackit_Product(
        String name    ) {
        super(
        );
        this.name = name;
        this.trackit_versions = new ArrayList<>();
    }

    public trackit_Product(
        String name        ArrayList<trackit_Version> trackit_versions    ) {
        this.name = name;
        this.trackit_versions = trackit_versions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<trackit_Version> getTrackit_versions() {
        return trackit_versions;
    }

    public void addTrackit_version(Trackit_version trackit_version) {
        this.trackit_versions.add(trackit_version);
    }
    public trackit_IssueTracker getTrackit_issuetracker() {
        return trackit_issuetracker;
    }

    public void setTrackit_issuetracker(trackit_IssueTracker trackit_issuetracker) {
        this.trackit_issuetracker = trackit_issuetracker;
    }
    public trackit_Version getTrackit_version() {
        return trackit_version;
    }

    public void setTrackit_version(trackit_Version trackit_version) {
        this.trackit_version = trackit_version;
    }

}