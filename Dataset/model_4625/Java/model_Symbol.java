





import java.util.List;
import java.util.ArrayList;

public class model_Symbol  {

    private String backgroundColor;
    private String onUpdate;
    private String onDispose;
    private String scriptModules;
    private String backgroundImage;
    private String onInit;





    private model_Dimension model_dimension;




    private model_Cursor model_cursor;


    public model_Symbol(
        String backgroundColor,        String onUpdate,        String onDispose,        String scriptModules,        String backgroundImage,        String onInit    ) {
        this.backgroundColor = backgroundColor;
        this.onUpdate = onUpdate;
        this.onDispose = onDispose;
        this.scriptModules = scriptModules;
        this.backgroundImage = backgroundImage;
        this.onInit = onInit;
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

    public model_Dimension getModel_dimension() {
        return model_dimension;
    }

    public void setModel_dimension(model_Dimension model_dimension) {
        this.model_dimension = model_dimension;
    }
    public model_Cursor getModel_cursor() {
        return model_cursor;
    }

    public void setModel_cursor(model_Cursor model_cursor) {
        this.model_cursor = model_cursor;
    }

}