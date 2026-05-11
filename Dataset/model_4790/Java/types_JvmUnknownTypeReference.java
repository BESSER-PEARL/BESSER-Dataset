





import java.util.List;
import java.util.ArrayList;

public class types_JvmUnknownTypeReference extends JvmTypeReference {

    private String exception;



    public types_JvmUnknownTypeReference(
        String exception    ) {
        super(
        );
        this.exception = exception;
    }


    public String getException() {
        return exception;
    }

    public void setException(String exception) {
        this.exception = exception;
    }


}