





import java.util.List;
import java.util.ArrayList;

public class SPL_SuccessResponse extends Response {

    private String successKind;



    public SPL_SuccessResponse(
        String successKind    ) {
        super(
        );
        this.successKind = successKind;
    }


    public String getSuccesskind() {
        return successKind;
    }

    public void setSuccesskind(String successKind) {
        this.successKind = successKind;
    }


}