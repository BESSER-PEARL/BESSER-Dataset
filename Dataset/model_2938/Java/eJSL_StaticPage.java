





import java.util.List;
import java.util.ArrayList;

public class eJSL_StaticPage extends Page {

    private String HTMLBody;
    private boolean preserve;



    public eJSL_StaticPage(
        String HTMLBody,        boolean preserve    ) {
        super(
        );
        this.HTMLBody = HTMLBody;
        this.preserve = preserve;
    }


    public String getHtmlbody() {
        return HTMLBody;
    }

    public void setHtmlbody(String HTMLBody) {
        this.HTMLBody = HTMLBody;
    }
    public boolean getPreserve() {
        return preserve;
    }

    public void setPreserve(boolean preserve) {
        this.preserve = preserve;
    }


}