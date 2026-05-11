





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Symbol  {

    private String onDispose;
    private String onInit;
    private String scriptModules;
    private String backgroundColor;
    private String onUpdate;



    public VisualInterface_Symbol(
        String onDispose,        String onInit,        String scriptModules,        String backgroundColor,        String onUpdate    ) {
        this.onDispose = onDispose;
        this.onInit = onInit;
        this.scriptModules = scriptModules;
        this.backgroundColor = backgroundColor;
        this.onUpdate = onUpdate;
    }


    public String getOndispose() {
        return onDispose;
    }

    public void setOndispose(String onDispose) {
        this.onDispose = onDispose;
    }
    public String getOninit() {
        return onInit;
    }

    public void setOninit(String onInit) {
        this.onInit = onInit;
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
    public String getOnupdate() {
        return onUpdate;
    }

    public void setOnupdate(String onUpdate) {
        this.onUpdate = onUpdate;
    }


}