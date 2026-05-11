





import java.util.List;
import java.util.ArrayList;

public class builds_BuildPlan extends BuildElement {

    private String id;
    private String flags;
    private boolean selected;
    private String summary;
    private String info;
    private int health;
    private String status;
    private String state;
    private String description;





    private builds_BuildPlan builds_buildplan;




    private List<builds_BuildPlan> builds_buildplans;




    private builds_BuildServer builds_buildserver;


    public builds_BuildPlan(
        String id,        String flags,        boolean selected,        String summary,        String info,        int health,        String status,        String state,        String description    ) {
        super(
        );
        this.id = id;
        this.flags = flags;
        this.selected = selected;
        this.summary = summary;
        this.info = info;
        this.health = health;
        this.status = status;
        this.state = state;
        this.description = description;
        this.builds_buildplans = new ArrayList<>();
    }

    public builds_BuildPlan(
        String id,        String flags,        boolean selected,        String summary,        String info,        int health,        String status,        String state,        String description        ArrayList<builds_BuildPlan> builds_buildplans    ) {
        this.id = id;
        this.flags = flags;
        this.selected = selected;
        this.summary = summary;
        this.info = info;
        this.health = health;
        this.status = status;
        this.state = state;
        this.description = description;
        this.builds_buildplans = builds_buildplans;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFlags() {
        return flags;
    }

    public void setFlags(String flags) {
        this.flags = flags;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }
    public List<builds_BuildPlan> getBuilds_buildplans() {
        return builds_buildplans;
    }

    public void addBuilds_buildplan(Builds_buildplan builds_buildplan) {
        this.builds_buildplans.add(builds_buildplan);
    }
    public builds_BuildServer getBuilds_buildserver() {
        return builds_buildserver;
    }

    public void setBuilds_buildserver(builds_BuildServer builds_buildserver) {
        this.builds_buildserver = builds_buildserver;
    }

}