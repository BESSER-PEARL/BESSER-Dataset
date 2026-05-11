





import java.util.List;
import java.util.ArrayList;

public class model_Symbol  {

    private String scriptModules;
    private String onDispose;
    private String onInit;
    private String onUpdate;
    private String backgroundColor;



    public model_Symbol(
        String scriptModules,        String onDispose,        String onInit,        String onUpdate,        String backgroundColor    ) {
        this.scriptModules = scriptModules;
        this.onDispose = onDispose;
        this.onInit = onInit;
        this.onUpdate = onUpdate;
        this.backgroundColor = backgroundColor;
    }


    public String getScriptmodules() {
        return scriptModules;
    }

    public void setScriptmodules(String scriptModules) {
        this.scriptModules = scriptModules;
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


}