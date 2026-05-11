





import java.util.List;
import java.util.ArrayList;

public class altarica_VectorParameter  {

    private boolean isRequired;





    private altarica_Vector altarica_vector;


    public altarica_VectorParameter(
        boolean isRequired    ) {
        this.isRequired = isRequired;
    }


    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }

    public altarica_Vector getAltarica_vector() {
        return altarica_vector;
    }

    public void setAltarica_vector(altarica_Vector altarica_vector) {
        this.altarica_vector = altarica_vector;
    }

}