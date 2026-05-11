





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Property extends Field {

    private boolean optional;





    private modelDsl_Type modeldsl_type;




    private modelDsl_EntityElements modeldsl_entityelements;


    public modelDsl_Property(
        boolean optional    ) {
        super(
        );
        this.optional = optional;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }

    public modelDsl_Type getModeldsl_type() {
        return modeldsl_type;
    }

    public void setModeldsl_type(modelDsl_Type modeldsl_type) {
        this.modeldsl_type = modeldsl_type;
    }
    public modelDsl_EntityElements getModeldsl_entityelements() {
        return modeldsl_entityelements;
    }

    public void setModeldsl_entityelements(modelDsl_EntityElements modeldsl_entityelements) {
        this.modeldsl_entityelements = modeldsl_entityelements;
    }

}