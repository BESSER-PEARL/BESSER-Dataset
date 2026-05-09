





import java.util.List;
import java.util.ArrayList;

public class mMDSL_ViewBox  {

    private String text;
    private String title;





    private mMDSL_SimpleUI mmdsl_simpleui;


    public mMDSL_ViewBox(
        String text,        String title    ) {
        this.text = text;
        this.title = title;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public mMDSL_SimpleUI getMmdsl_simpleui() {
        return mmdsl_simpleui;
    }

    public void setMmdsl_simpleui(mMDSL_SimpleUI mmdsl_simpleui) {
        this.mmdsl_simpleui = mmdsl_simpleui;
    }

}