





import java.util.List;
import java.util.ArrayList;

public class scmodel_AbstractState  {

    private String onEnter;
    private String id;
    private String onExitImports;
    private String language;
    private String uuid;
    private String onExit;
    private String onEnterImports;





    private scmodel_StateMachine scmodel_statemachine;


    public scmodel_AbstractState(
        String onEnter,        String id,        String onExitImports,        String language,        String uuid,        String onExit,        String onEnterImports    ) {
        this.onEnter = onEnter;
        this.id = id;
        this.onExitImports = onExitImports;
        this.language = language;
        this.uuid = uuid;
        this.onExit = onExit;
        this.onEnterImports = onEnterImports;
    }


    public String getOnenter() {
        return onEnter;
    }

    public void setOnenter(String onEnter) {
        this.onEnter = onEnter;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getOnexitimports() {
        return onExitImports;
    }

    public void setOnexitimports(String onExitImports) {
        this.onExitImports = onExitImports;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public String getOnexit() {
        return onExit;
    }

    public void setOnexit(String onExit) {
        this.onExit = onExit;
    }
    public String getOnenterimports() {
        return onEnterImports;
    }

    public void setOnenterimports(String onEnterImports) {
        this.onEnterImports = onEnterImports;
    }

    public scmodel_StateMachine getScmodel_statemachine() {
        return scmodel_statemachine;
    }

    public void setScmodel_statemachine(scmodel_StateMachine scmodel_statemachine) {
        this.scmodel_statemachine = scmodel_statemachine;
    }

}