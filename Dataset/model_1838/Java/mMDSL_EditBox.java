





import java.util.List;
import java.util.ArrayList;

public class mMDSL_EditBox  {

    private String title;
    private String okbuttontext;
    private String text;





    private mMDSL_SimpleUI mmdsl_simpleui;


    public mMDSL_EditBox(
        String title,        String okbuttontext,        String text    ) {
        this.title = title;
        this.okbuttontext = okbuttontext;
        this.text = text;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getOkbuttontext() {
        return okbuttontext;
    }

    public void setOkbuttontext(String okbuttontext) {
        this.okbuttontext = okbuttontext;
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