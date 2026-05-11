





import java.util.List;
import java.util.ArrayList;

public class oclstdlibcs_LibOperationCS extends OperationCS, JavaImplementationCS {

    private String isInvalidating;
    private String isValidating;
    private String isStatic;



    public oclstdlibcs_LibOperationCS(
        String isInvalidating,        String isValidating,        String isStatic    ) {
        super(
        );
        this.isInvalidating = isInvalidating;
        this.isValidating = isValidating;
        this.isStatic = isStatic;
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
    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }


}