





import java.util.List;
import java.util.ArrayList;

public class SPL_RedirectionErrorResponse extends ErrorResponse {

    private String errorKind;



    public SPL_RedirectionErrorResponse(
        String errorKind    ) {
        super(
        );
        this.errorKind = errorKind;
    }


    public String getErrorkind() {
        return errorKind;
    }

    public void setErrorkind(String errorKind) {
        this.errorKind = errorKind;
    }


}