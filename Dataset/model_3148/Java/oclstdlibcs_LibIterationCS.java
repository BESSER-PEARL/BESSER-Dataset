





import java.util.List;
import java.util.ArrayList;

public class oclstdlibcs_LibIterationCS extends OperationCS, JavaImplementationCS {

    private String isInvalidating;
    private String isValidating;



    public oclstdlibcs_LibIterationCS(
        String isInvalidating,        String isValidating    ) {
        super(
        );
        this.isInvalidating = isInvalidating;
        this.isValidating = isValidating;
    }


    public String getIsinvalidating() {
        return isInvalidating;
    }

    public void setIsinvalidating(String isInvalidating) {
        this.isInvalidating = isInvalidating;
    }
    public String getIsvalidating() {
        return isValidating;
    }

    public void setIsvalidating(String isValidating) {
        this.isValidating = isValidating;
    }


}