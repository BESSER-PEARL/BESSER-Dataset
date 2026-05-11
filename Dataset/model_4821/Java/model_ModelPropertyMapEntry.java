





import java.util.List;
import java.util.ArrayList;

public class model_ModelPropertyMapEntry  {

    private String key;





    private model_ModelProperty model_modelproperty;


    public model_ModelPropertyMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public model_ModelProperty getModel_modelproperty() {
        return model_modelproperty;
    }

    public void setModel_modelproperty(model_ModelProperty model_modelproperty) {
        this.model_modelproperty = model_modelproperty;
    }

}