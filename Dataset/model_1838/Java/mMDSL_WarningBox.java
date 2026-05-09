





import java.util.List;
import java.util.ArrayList;

public class mMDSL_WarningBox  {

    private String title;
    private String buttontype;
    private String text;





    private mMDSL_SimpleUI mmdsl_simpleui;


    public mMDSL_WarningBox(
        String title,        String buttontype,        String text    ) {
        this.title = title;
        this.buttontype = buttontype;
        this.text = text;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getButtontype() {
        return buttontype;
    }

    public void setButtontype(String buttontype) {
        this.buttontype = buttontype;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public mMDSL_SimpleUI getMmdsl_simpleui() {
        return mmdsl_simpleui;
    }

    public void setMmdsl_simpleui(mMDSL_SimpleUI mmdsl_simpleui) {
        this.mmdsl_simpleui = mmdsl_simpleui;
    }

}