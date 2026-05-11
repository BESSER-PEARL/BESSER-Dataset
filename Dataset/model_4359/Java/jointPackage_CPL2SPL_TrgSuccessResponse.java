





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgSuccessResponse extends TrgResponse {

    private String successKind;



    public jointPackage_CPL2SPL_TrgSuccessResponse(
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