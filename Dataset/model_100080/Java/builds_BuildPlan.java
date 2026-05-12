





import java.util.List;
import java.util.ArrayList;

public class builds_BuildPlan extends BuildElement {

    private String info;
    private String flags;
    private String status;
    private int health;
    private String state;
    private String description;
    private String summary;
    private String id;
    private boolean selected;





    private builds_BuildServer builds_buildserver;




    private builds_BuildPlan builds_buildplan;




    private builds_BuildPlan builds_buildplan;


    public builds_BuildPlan(
        String info,        String flags,        String status,        int health,        String state,        String description,        String summary,        String id,        boolean selected    ) {
        super(
        );
        this.info = info;
        this.flags = flags;
        this.status = status;
        this.health = health;
        this.state = state;
        this.description = description;
        this.summary = summary;
        this.id = id;
        this.selected = selected;
    }


    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
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
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
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
    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }

}