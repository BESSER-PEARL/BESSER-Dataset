





import java.util.List;
import java.util.ArrayList;

public class scmodel_StateMachine  {

    private String agentType;
    private String className;
    private String package;
    private int nextID;
    private String uuid;
    private String id;
    private float priority;
    private String language;



    public scmodel_StateMachine(
        String agentType,        String className,        String package,        int nextID,        String uuid,        String id,        float priority,        String language    ) {
        this.agentType = agentType;
        this.className = className;
        this.package = package;
        this.nextID = nextID;
        this.uuid = uuid;
        this.id = id;
        this.priority = priority;
        this.language = language;
    }


    public String getAgenttype() {
        return agentType;
    }

    public void setAgenttype(String agentType) {
        this.agentType = agentType;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public int getNextid() {
        return nextID;
    }

    public void setNextid(int nextID) {
        this.nextID = nextID;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public float getPriority() {
        return priority;
    }

    public void setPriority(float priority) {
        this.priority = priority;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}