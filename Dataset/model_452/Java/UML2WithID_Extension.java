





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Extension extends Association {

    private boolean isRequired;



    public UML2WithID_Extension(
        boolean isRequired    ) {
        super(
        );
        this.isRequired = isRequired;
    }


    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }


}