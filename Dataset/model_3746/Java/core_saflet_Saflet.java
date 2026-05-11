





import java.util.List;
import java.util.ArrayList;

public class core_saflet_Saflet extends ThreadSensitive, PlatformDisposition {

    private String description;
    private int id;
    private String version;
    private boolean active;
    private String name;





    private SafletContext safletcontext;




    private SafletScriptEnvironment safletscriptenvironment;




    private ScriptScope scriptscope;




    private Initiator initiator;


    public core_saflet_Saflet(
        String description,        int id,        String version,        boolean active,        String name    ) {
        super(
        );
        this.description = description;
        this.id = id;
        this.version = version;
        this.active = active;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SafletContext getSafletcontext() {
        return safletcontext;
    }

    public void setSafletcontext(SafletContext safletcontext) {
        this.safletcontext = safletcontext;
    }
    public SafletScriptEnvironment getSafletscriptenvironment() {
        return safletscriptenvironment;
    }

    public void setSafletscriptenvironment(SafletScriptEnvironment safletscriptenvironment) {
        this.safletscriptenvironment = safletscriptenvironment;
    }
    public ScriptScope getScriptscope() {
        return scriptscope;
    }

    public void setScriptscope(ScriptScope scriptscope) {
        this.scriptscope = scriptscope;
    }
    public Initiator getInitiator() {
        return initiator;
    }

    public void setInitiator(Initiator initiator) {
        this.initiator = initiator;
    }

}