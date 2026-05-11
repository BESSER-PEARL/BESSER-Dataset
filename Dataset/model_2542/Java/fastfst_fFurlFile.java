





import java.util.List;
import java.util.ArrayList;

public class fastfst_fFurlFile  {

    private String value;
    private String name;





    private fastfst_ModelFastfst fastfst_modelfastfst;


    public fastfst_fFurlFile(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fastfst_ModelFastfst getFastfst_modelfastfst() {
        return fastfst_modelfastfst;
    }

    public void setFastfst_modelfastfst(fastfst_ModelFastfst fastfst_modelfastfst) {
        this.fastfst_modelfastfst = fastfst_modelfastfst;
    }

}