





import java.util.List;
import java.util.ArrayList;

public class model_Symbol  {

    private String scriptModules;
    private String backgroundColor;
    private String onDispose;
    private String onUpdate;
    private String backgroundImage;
    private String onInit;





    private List<model_Connection> model_connections;


    public model_Symbol(
        String scriptModules,        String backgroundColor,        String onDispose,        String onUpdate,        String backgroundImage,        String onInit    ) {
        this.scriptModules = scriptModules;
        this.backgroundColor = backgroundColor;
        this.onDispose = onDispose;
        this.onUpdate = onUpdate;
        this.backgroundImage = backgroundImage;
        this.onInit = onInit;
        this.model_connections = new ArrayList<>();
    }

    public model_Symbol(
        String scriptModules,        String backgroundColor,        String onDispose,        String onUpdate,        String backgroundImage,        String onInit        ArrayList<model_Connection> model_connections    ) {
        this.scriptModules = scriptModules;
        this.backgroundColor = backgroundColor;
        this.onDispose = onDispose;
        this.onUpdate = onUpdate;
        this.backgroundImage = backgroundImage;
        this.onInit = onInit;
        this.model_connections = model_connections;
    }

    public String getScriptmodules() {
        return scriptModules;
    }

    public void setScriptmodules(String scriptModules) {
        this.scriptModules = scriptModules;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getOndispose() {
        return onDispose;
    }

    public void setOndispose(String onDispose) {
        this.onDispose = onDispose;
    }
    public String getOnupdate() {
        return onUpdate;
    }

    public void setOnupdate(String onUpdate) {
        this.onUpdate = onUpdate;
    }
    public String getBackgroundimage() {
        return backgroundImage;
    }

    public void setBackgroundimage(String backgroundImage) {
        this.backgroundImage = backgroundImage;
    }
    public String getOninit() {
        return onInit;
    }

    public void setOninit(String onInit) {
        this.onInit = onInit;
    }

    public List<model_Connection> getModel_connections() {
        return model_connections;
    }

    public void addModel_connection(Model_connection model_connection) {
        this.model_connections.add(model_connection);
    }

}