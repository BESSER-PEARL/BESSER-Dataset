





import java.util.List;
import java.util.ArrayList;

public class cevinedit_PersonalizedElement  {

    private String icon;
    private String name;





    private cevinedit_Diagram cevinedit_diagram;


    public cevinedit_PersonalizedElement(
        String icon,        String name    ) {
        this.icon = icon;
        this.name = name;
    }


    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cevinedit_Diagram getCevinedit_diagram() {
        return cevinedit_diagram;
    }

    public void setCevinedit_diagram(cevinedit_Diagram cevinedit_diagram) {
        this.cevinedit_diagram = cevinedit_diagram;
    }

}