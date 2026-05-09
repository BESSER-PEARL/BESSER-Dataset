





import java.util.List;
import java.util.ArrayList;

public class SMVC_View  {

    private String text;





    private SMVC_Page smvc_page;


    public SMVC_View(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public SMVC_Page getSmvc_page() {
        return smvc_page;
    }

    public void setSmvc_page(SMVC_Page smvc_page) {
        this.smvc_page = smvc_page;
    }

}