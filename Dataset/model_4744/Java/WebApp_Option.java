





import java.util.List;
import java.util.ArrayList;

public class WebApp_Option  {

    private int fraction;
    private String text;





    private WebApp_Multiple webapp_multiple;


    public WebApp_Option(
        int fraction,        String text    ) {
        this.fraction = fraction;
        this.text = text;
    }


    public int getFraction() {
        return fraction;
    }

    public void setFraction(int fraction) {
        this.fraction = fraction;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public WebApp_Multiple getWebapp_multiple() {
        return webapp_multiple;
    }

    public void setWebapp_multiple(WebApp_Multiple webapp_multiple) {
        this.webapp_multiple = webapp_multiple;
    }

}