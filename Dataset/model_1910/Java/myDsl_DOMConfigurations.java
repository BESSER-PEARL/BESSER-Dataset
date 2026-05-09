





import java.util.List;
import java.util.ArrayList;

public class myDsl_DOMConfigurations  {

    private String name;
    private String elements;





    private myDsl_ReactConfigurations mydsl_reactconfigurations;


    public myDsl_DOMConfigurations(
        String name,        String elements    ) {
        this.name = name;
        this.elements = elements;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getElements() {
        return elements;
    }

    public void setElements(String elements) {
        this.elements = elements;
    }

    public myDsl_ReactConfigurations getMydsl_reactconfigurations() {
        return mydsl_reactconfigurations;
    }

    public void setMydsl_reactconfigurations(myDsl_ReactConfigurations mydsl_reactconfigurations) {
        this.mydsl_reactconfigurations = mydsl_reactconfigurations;
    }

}