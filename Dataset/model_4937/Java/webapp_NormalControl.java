





import java.util.List;
import java.util.ArrayList;

public class webapp_NormalControl extends Control {

    private String text;





    private webapp_NormalPage webapp_normalpage;


    public webapp_NormalControl(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public webapp_NormalPage getWebapp_normalpage() {
        return webapp_normalpage;
    }

    public void setWebapp_normalpage(webapp_NormalPage webapp_normalpage) {
        this.webapp_normalpage = webapp_normalpage;
    }

}