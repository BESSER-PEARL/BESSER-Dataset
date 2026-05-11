





import java.util.List;
import java.util.ArrayList;

public class model_requirements_CEGConnection extends IModelConnection {

    private boolean negate;



    public model_requirements_CEGConnection(
        boolean negate    ) {
        super(
        );
        this.negate = negate;
    }


    public boolean getNegate() {
        return negate;
    }

    public void setNegate(boolean negate) {
        this.negate = negate;
    }


}