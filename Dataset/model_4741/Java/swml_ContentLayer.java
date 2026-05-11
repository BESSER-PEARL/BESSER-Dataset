





import java.util.List;
import java.util.ArrayList;

public class swml_ContentLayer  {






    private swml_WebModel swml_webmodel;




    private List<swml_Class> swml_classs;


    public swml_ContentLayer(
    ) {
        this.swml_classs = new ArrayList<>();
    }

    public swml_ContentLayer(
        ArrayList<swml_Class> swml_classs    ) {
        this.swml_classs = swml_classs;
    }


    public swml_WebModel getSwml_webmodel() {
        return swml_webmodel;
    }

    public void setSwml_webmodel(swml_WebModel swml_webmodel) {
        this.swml_webmodel = swml_webmodel;
    }
    public List<swml_Class> getSwml_classs() {
        return swml_classs;
    }

    public void addSwml_class(Swml_class swml_class) {
        this.swml_classs.add(swml_class);
    }

}