





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Setting  {

    private boolean alwaysvectorfont;
    private String verticaltext;





    private eaglemodel_Settings eaglemodel_settings;


    public eaglemodel_Setting(
        boolean alwaysvectorfont,        String verticaltext    ) {
        this.alwaysvectorfont = alwaysvectorfont;
        this.verticaltext = verticaltext;
    }


    public boolean getAlwaysvectorfont() {
        return alwaysvectorfont;
    }

    public void setAlwaysvectorfont(boolean alwaysvectorfont) {
        this.alwaysvectorfont = alwaysvectorfont;
    }
    public String getVerticaltext() {
        return verticaltext;
    }

    public void setVerticaltext(String verticaltext) {
        this.verticaltext = verticaltext;
    }

    public eaglemodel_Settings getEaglemodel_settings() {
        return eaglemodel_settings;
    }

    public void setEaglemodel_settings(eaglemodel_Settings eaglemodel_settings) {
        this.eaglemodel_settings = eaglemodel_settings;
    }

}