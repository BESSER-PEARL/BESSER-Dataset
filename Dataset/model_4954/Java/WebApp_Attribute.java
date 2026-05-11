





import java.util.List;
import java.util.ArrayList;

public class WebApp_Attribute extends NamedElement {

    private String value;





    private WebApp_Dummies webapp_dummies;


    public WebApp_Attribute(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public WebApp_Dummies getWebapp_dummies() {
        return webapp_dummies;
    }

    public void setWebapp_dummies(WebApp_Dummies webapp_dummies) {
        this.webapp_dummies = webapp_dummies;
    }

}