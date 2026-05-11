





import java.util.List;
import java.util.ArrayList;

public class builds_Build extends BuildElement {

    private String id;
    private String summary;
    private String duration;
    private String timestamp;
    private String label;
    private String status;
    private int buildNumber;
    private String state;
    private String displayName;





    private builds_BuildPlan builds_buildplan;




    private builds_BuildServer builds_buildserver;




    private List<builds_User> builds_users;




    private List<builds_Artifact> builds_artifacts;




    private builds_BuildPlan builds_buildplan;




    private builds_ChangeSet builds_changeset;


    public builds_Build(
        String id,        String summary,        String duration,        String timestamp,        String label,        String status,        int buildNumber,        String state,        String displayName    ) {
        super(
        );
        this.id = id;
        this.summary = summary;
        this.duration = duration;
        this.timestamp = timestamp;
        this.label = label;
        this.status = status;
        this.buildNumber = buildNumber;
        this.state = state;
        this.displayName = displayName;
        this.builds_users = new ArrayList<>();
        this.builds_artifacts = new ArrayList<>();
    }

    public builds_Build(
        String id,        String summary,        String duration,        String timestamp,        String label,        String status,        int buildNumber,        String state,        String displayName        ArrayList<builds_User> builds_users,        ArrayList<builds_Artifact> builds_artifacts    ) {
        this.id = id;
        this.summary = summary;
        this.duration = duration;
        this.timestamp = timestamp;
        this.label = label;
        this.status = status;
        this.buildNumber = buildNumber;
        this.state = state;
        this.displayName = displayName;
        this.builds_users = builds_users;
        this.builds_artifacts = builds_artifacts;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getBuildnumber() {
        return buildNumber;
    }

    public void setBuildnumber(int buildNumber) {
        this.buildNumber = buildNumber;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }

    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }
    public builds_BuildServer getBuilds_buildserver() {
        return builds_buildserver;
    }

    public void setBuilds_buildserver(builds_BuildServer builds_buildserver) {
        this.builds_buildserver = builds_buildserver;
    }
    public List<builds_User> getBuilds_users() {
        return builds_users;
    }

    public void addBuilds_user(Builds_user builds_user) {
        this.builds_users.add(builds_user);
    }
    public List<builds_Artifact> getBuilds_artifacts() {
        return builds_artifacts;
    }

    public void addBuilds_artifact(Builds_artifact builds_artifact) {
        this.builds_artifacts.add(builds_artifact);
    }
    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }
    public builds_ChangeSet getBuilds_changeset() {
        return builds_changeset;
    }

    public void setBuilds_changeset(builds_ChangeSet builds_changeset) {
        this.builds_changeset = builds_changeset;
    }

}