





import java.util.List;
import java.util.ArrayList;

public class fastfst_bYawDOF  {

    private String name;
    private boolean value;





    private fastfst_ModelFastfst fastfst_modelfastfst;


    public fastfst_bYawDOF(
        String name,        boolean value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public fastfst_ModelFastfst getFastfst_modelfastfst() {
        return fastfst_modelfastfst;
    }

    public void setFastfst_modelfastfst(fastfst_ModelFastfst fastfst_modelfastfst) {
        this.fastfst_modelfastfst = fastfst_modelfastfst;
    }

}