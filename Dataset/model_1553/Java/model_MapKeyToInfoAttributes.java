





import java.util.List;
import java.util.ArrayList;

public class model_MapKeyToInfoAttributes  {

    private String key;
    private String value;





    private model_R4EFileVersion model_r4efileversion;




    private model_R4EItem model_r4eitem;




    private model_R4EComment model_r4ecomment;




    private model_R4EFileContext model_r4efilecontext;


    public model_MapKeyToInfoAttributes(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public model_R4EFileVersion getModel_r4efileversion() {
        return model_r4efileversion;
    }

    public void setModel_r4efileversion(model_R4EFileVersion model_r4efileversion) {
        this.model_r4efileversion = model_r4efileversion;
    }
    public model_R4EItem getModel_r4eitem() {
        return model_r4eitem;
    }

    public void setModel_r4eitem(model_R4EItem model_r4eitem) {
        this.model_r4eitem = model_r4eitem;
    }
    public model_R4EComment getModel_r4ecomment() {
        return model_r4ecomment;
    }

    public void setModel_r4ecomment(model_R4EComment model_r4ecomment) {
        this.model_r4ecomment = model_r4ecomment;
    }
    public model_R4EFileContext getModel_r4efilecontext() {
        return model_r4efilecontext;
    }

    public void setModel_r4efilecontext(model_R4EFileContext model_r4efilecontext) {
        this.model_r4efilecontext = model_r4efilecontext;
    }

}