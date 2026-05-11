





import java.util.List;
import java.util.ArrayList;

public class rcd_Attribute  {

    private boolean is_primary;
    private String name;
    private String upper;
    private String lower;





    private rcd_Class rcd_class;




    private rcd_Classifier rcd_classifier;


    public rcd_Attribute(
        boolean is_primary,        String name,        String upper,        String lower    ) {
        this.is_primary = is_primary;
        this.name = name;
        this.upper = upper;
        this.lower = lower;
    }


    public boolean getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(boolean is_primary) {
        this.is_primary = is_primary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }

    public rcd_Class getRcd_class() {
        return rcd_class;
    }

    public void setRcd_class(rcd_Class rcd_class) {
        this.rcd_class = rcd_class;
    }
    public rcd_Classifier getRcd_classifier() {
        return rcd_classifier;
    }

    public void setRcd_classifier(rcd_Classifier rcd_classifier) {
        this.rcd_classifier = rcd_classifier;
    }

}