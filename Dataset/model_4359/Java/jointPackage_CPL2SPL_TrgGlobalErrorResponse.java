





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgGlobalErrorResponse extends TrgErrorResponse {

    private String errorKind;



    public jointPackage_CPL2SPL_TrgGlobalErrorResponse(
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