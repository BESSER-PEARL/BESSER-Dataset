





import java.util.List;
import java.util.ArrayList;

public class builds_Build extends BuildElement {

    private String state;
    private int buildNumber;
    private String status;
    private String label;
    private String duration;
    private String summary;
    private String displayName;
    private String id;
    private String timestamp;





    private List<builds_Artifact> builds_artifacts;




    private builds_TestResult builds_testresult;




    private builds_BuildPlan builds_buildplan;




    private builds_TestResult builds_testresult;




    private List<builds_User> builds_users;




    private builds_BuildServer builds_buildserver;




    private List<builds_BuildCause> builds_buildcauses;




    private builds_BuildPlan builds_buildplan;


    public builds_Build(
        String state,        int buildNumber,        String status,        String label,        String duration,        String summary,        String displayName,        String id,        String timestamp    ) {
        super(
        );
        this.state = state;
        this.buildNumber = buildNumber;
        this.status = status;
        this.label = label;
        this.duration = duration;
        this.summary = summary;
        this.displayName = displayName;
        this.id = id;
        this.timestamp = timestamp;
        this.builds_artifacts = new ArrayList<>();
        this.builds_users = new ArrayList<>();
        this.builds_buildcauses = new ArrayList<>();
    }

    public builds_Build(
        String state,        int buildNumber,        String status,        String label,        String duration,        String summary,        String displayName,        String id,        String timestamp        ArrayList<builds_Artifact> builds_artifacts,        ArrayList<builds_User> builds_users,        ArrayList<builds_BuildCause> builds_buildcauses    ) {
        this.state = state;
        this.buildNumber = buildNumber;
        this.status = status;
        this.label = label;
        this.duration = duration;
        this.summary = summary;
        this.displayName = displayName;
        this.id = id;
        this.timestamp = timestamp;
        this.builds_artifacts = builds_artifacts;
        this.builds_users = builds_users;
        this.builds_buildcauses = builds_buildcauses;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
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
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public List<builds_Artifact> getBuilds_artifacts() {
        return builds_artifacts;
    }

    public void addBuilds_artifact(Builds_artifact builds_artifact) {
        this.builds_artifacts.add(builds_artifact);
    }
    public builds_TestResult getBuilds_testresult() {
        return builds_testresult;
    }

    public void setBuilds_testresult(builds_TestResult builds_testresult) {
        this.builds_testresult = builds_testresult;
    }
    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }
    public builds_TestResult getBuilds_testresult() {
        return builds_testresult;
    }

    public void setBuilds_testresult(builds_TestResult builds_testresult) {
        this.builds_testresult = builds_testresult;
    }
    public List<builds_User> getBuilds_users() {
        return builds_users;
    }

    public void addBuilds_user(Builds_user builds_user) {
        this.builds_users.add(builds_user);
    }
    public builds_BuildServer getBuilds_buildserver() {
        return builds_buildserver;
    }

    public void setBuilds_buildserver(builds_BuildServer builds_buildserver) {
        this.builds_buildserver = builds_buildserver;
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

}