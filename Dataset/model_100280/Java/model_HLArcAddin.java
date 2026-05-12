





import java.util.List;
import java.util.ArrayList;

public class model_HLArcAddin  {

    private String type;





    private model_HLAnnotation model_hlannotation;


    public model_HLArcAddin(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public model_HLAnnotation getModel_hlannotation() {
        return model_hlannotation;
    }

    public void setModel_hlannotation(model_HLAnnotation model_hlannotation) {
        this.model_hlannotation = model_hlannotation;
    }

}