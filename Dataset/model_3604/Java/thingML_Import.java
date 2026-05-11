





import java.util.List;
import java.util.ArrayList;

public class thingML_Import  {

    private String from_;
    private String importURI;





    private thingML_ThingMLModel thingml_thingmlmodel;


    public thingML_Import(
        String from_,        String importURI    ) {
        this.from_ = from_;
        this.importURI = importURI;
    }


    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public thingML_ThingMLModel getThingml_thingmlmodel() {
        return thingml_thingmlmodel;
    }

    public void setThingml_thingmlmodel(thingML_ThingMLModel thingml_thingmlmodel) {
        this.thingml_thingmlmodel = thingml_thingmlmodel;
    }

}