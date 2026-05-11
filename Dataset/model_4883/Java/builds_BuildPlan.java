





import java.util.List;
import java.util.ArrayList;

public class builds_BuildPlan extends BuildElement {

    private String summary;
    private String id;
    private String flags;
    private String status;
    private int health;
    private String info;
    private String description;
    private boolean selected;
    private String state;





    private builds_BuildPlan builds_buildplan;




    private builds_BuildServer builds_buildserver;




    private List<builds_BuildPlan> builds_buildplans;


    public builds_BuildPlan(
        String summary,        String id,        String flags,        String status,        int health,        String info,        String description,        boolean selected,        String state    ) {
        super(
        );
        this.summary = summary;
        this.id = id;
        this.flags = flags;
        this.status = status;
        this.health = health;
        this.info = info;
        this.description = description;
        this.selected = selected;
        this.state = state;
        this.builds_buildplans = new ArrayList<>();
    }

    public builds_BuildPlan(
        String summary,        String id,        String flags,        String status,        int health,        String info,        String description,        boolean selected,        String state        ArrayList<builds_BuildPlan> builds_buildplans    ) {
        this.summary = summary;
        this.id = id;
        this.flags = flags;
        this.status = status;
        this.health = health;
        this.info = info;
        this.description = description;
        this.selected = selected;
        this.state = state;
        this.builds_buildplans = builds_buildplans;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
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
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
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
    public List<builds_BuildPlan> getBuilds_buildplans() {
        return builds_buildplans;
    }

    public void addBuilds_buildplan(Builds_buildplan builds_buildplan) {
        this.builds_buildplans.add(builds_buildplan);
    }

}