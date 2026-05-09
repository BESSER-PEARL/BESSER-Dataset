





import java.util.List;
import java.util.ArrayList;

public class webapp_Template extends NamedElement {

    private String structure;
    private String style;





    private webapp_WebApp webapp_webapp;




    private webapp_View webapp_view;


    public webapp_Template(
        String structure,        String style    ) {
        super(
        );
        this.structure = structure;
        this.style = style;
    }


    public String getStructure() {
        return structure;
    }

    public void setStructure(String structure) {
        this.structure = structure;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public webapp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(webapp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }
    public webapp_View getWebapp_view() {
        return webapp_view;
    }

    public void setWebapp_view(webapp_View webapp_view) {
        this.webapp_view = webapp_view;
    }

}