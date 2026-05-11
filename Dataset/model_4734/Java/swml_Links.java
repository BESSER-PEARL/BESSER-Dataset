





import java.util.List;
import java.util.ArrayList;

public class swml_Links  {

    private String Name;





    private swml_WebPage swml_webpage;


    public swml_Links(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public swml_WebPage getSwml_webpage() {
        return swml_webpage;
    }

    public void setSwml_webpage(swml_WebPage swml_webpage) {
        this.swml_webpage = swml_webpage;
    }

}