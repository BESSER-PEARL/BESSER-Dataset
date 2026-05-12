





import java.util.List;
import java.util.ArrayList;

public class model_HLArcAddin  {

    private String kind;





    private model_HLAnnotation model_hlannotation;


    public model_HLArcAddin(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public model_HLAnnotation getModel_hlannotation() {
        return model_hlannotation;
    }

    public void setModel_hlannotation(model_HLAnnotation model_hlannotation) {
        this.model_hlannotation = model_hlannotation;
    }

}