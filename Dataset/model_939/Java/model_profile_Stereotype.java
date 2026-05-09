





import java.util.List;
import java.util.ArrayList;

public class model_profile_Stereotype extends UnicaseModelElement {

    private boolean required;



    public model_profile_Stereotype(
        boolean required    ) {
        super(
        );
        this.required = required;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }


}