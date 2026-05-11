





import java.util.List;
import java.util.ArrayList;

public class fastfst_iPtfmModel  {

    private int value;
    private String name;





    private fastfst_ModelFastfst fastfst_modelfastfst;


    public fastfst_iPtfmModel(
        int value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
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