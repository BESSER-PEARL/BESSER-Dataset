





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Symbol  {

    private String onDispose;
    private String scriptModules;
    private String onUpdate;
    private String backgroundColor;
    private String onInit;



    public VisualInterface_Symbol(
        String onDispose,        String scriptModules,        String onUpdate,        String backgroundColor,        String onInit    ) {
        this.onDispose = onDispose;
        this.scriptModules = scriptModules;
        this.onUpdate = onUpdate;
        this.backgroundColor = backgroundColor;
        this.onInit = onInit;
    }


    public String getOndispose() {
        return onDispose;
    }

    public void setOndispose(String onDispose) {
        this.onDispose = onDispose;
    }
    public String getScriptmodules() {
        return scriptModules;
    }

    public void setScriptmodules(String scriptModules) {
        this.scriptModules = scriptModules;
    }
    public String getOnupdate() {
        return onUpdate;
    }

    public void setOnupdate(String onUpdate) {
        this.onUpdate = onUpdate;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getOninit() {
        return onInit;
    }

    public void setOninit(String onInit) {
        this.onInit = onInit;
    }


}