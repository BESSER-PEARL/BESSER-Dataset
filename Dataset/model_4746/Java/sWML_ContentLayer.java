





import java.util.List;
import java.util.ArrayList;

public class sWML_ContentLayer  {






    private sWML_WebModel swml_webmodel;




    private List<sWML_Class> swml_classs;


    public sWML_ContentLayer(
    ) {
        this.swml_classs = new ArrayList<>();
    }

    public sWML_ContentLayer(
        ArrayList<sWML_Class> swml_classs    ) {
        this.swml_classs = swml_classs;
    }


    public sWML_WebModel getSwml_webmodel() {
        return swml_webmodel;
    }

    public void setSwml_webmodel(sWML_WebModel swml_webmodel) {
        this.swml_webmodel = swml_webmodel;
    }
    public List<sWML_Class> getSwml_classs() {
        return swml_classs;
    }

    public void addSwml_class(Swml_class swml_class) {
        this.swml_classs.add(swml_class);
    }

}