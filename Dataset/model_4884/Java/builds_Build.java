





import java.util.List;
import java.util.ArrayList;

public class builds_Build extends BuildElement {

    private String id;
    private String displayName;
    private String summary;
    private String duration;
    private String label;
    private int buildNumber;
    private String status;
    private String timestamp;
    private String state;





    private builds_TestResult builds_testresult;




    private builds_BuildServer builds_buildserver;




    private builds_BuildPlan builds_buildplan;




    private List<builds_Artifact> builds_artifacts;




    private List<builds_BuildCause> builds_buildcauses;




    private builds_BuildPlan builds_buildplan;




    private List<builds_User> builds_users;




    private builds_TestResult builds_testresult;


    public builds_Build(
        String id,        String displayName,        String summary,        String duration,        String label,        int buildNumber,        String status,        String timestamp,        String state    ) {
        super(
        );
        this.id = id;
        this.displayName = displayName;
        this.summary = summary;
        this.duration = duration;
        this.label = label;
        this.buildNumber = buildNumber;
        this.status = status;
        this.timestamp = timestamp;
        this.state = state;
        this.builds_artifacts = new ArrayList<>();
        this.builds_buildcauses = new ArrayList<>();
        this.builds_users = new ArrayList<>();
    }

    public builds_Build(
        String id,        String displayName,        String summary,        String duration,        String label,        int buildNumber,        String status,        String timestamp,        String state        ArrayList<builds_Artifact> builds_artifacts,        ArrayList<builds_BuildCause> builds_buildcauses,        ArrayList<builds_User> builds_users    ) {
        this.id = id;
        this.displayName = displayName;
        this.summary = summary;
        this.duration = duration;
        this.label = label;
        this.buildNumber = buildNumber;
        this.status = status;
        this.timestamp = timestamp;
        this.state = state;
        this.builds_artifacts = builds_artifacts;
        this.builds_buildcauses = builds_buildcauses;
        this.builds_users = builds_users;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
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
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public int getBuildnumber() {
        return buildNumber;
    }

    public void setBuildnumber(int buildNumber) {
        this.buildNumber = buildNumber;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public builds_TestResult getBuilds_testresult() {
        return builds_testresult;
    }

    public void setBuilds_testresult(builds_TestResult builds_testresult) {
        this.builds_testresult = builds_testresult;
    }
    public builds_BuildServer getBuilds_buildserver() {
        return builds_buildserver;
    }

    public void setBuilds_buildserver(builds_BuildServer builds_buildserver) {
        this.builds_buildserver = builds_buildserver;
    }
    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }
    public List<builds_Artifact> getBuilds_artifacts() {
        return builds_artifacts;
    }

    public void addBuilds_artifact(Builds_artifact builds_artifact) {
        this.builds_artifacts.add(builds_artifact);
    }
    public List<builds_BuildCause> getBuilds_buildcauses() {
        return builds_buildcauses;
    }

    public void addBuilds_buildcause(Builds_buildcause builds_buildcause) {
        this.builds_buildcauses.add(builds_buildcause);
    }
    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }
    public List<builds_User> getBuilds_users() {
        return builds_users;
    }

    public void addBuilds_user(Builds_user builds_user) {
        this.builds_users.add(builds_user);
    }
    public builds_TestResult getBuilds_testresult() {
        return builds_testresult;
    }

    public void setBuilds_testresult(builds_TestResult builds_testresult) {
        this.builds_testresult = builds_testresult;
    }

}