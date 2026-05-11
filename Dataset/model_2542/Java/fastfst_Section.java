





import java.util.List;
import java.util.ArrayList;

public class fastfst_Section  {

    private String name;





    private fastfst_ModelFastfst fastfst_modelfastfst;


    public fastfst_Section(
        String name    ) {
        this.name = name;
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