





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserSavePast extends UserAction {

    private String destPath;



    public spinefm_UserActionModel_UserSavePast(
        String destPath    ) {
        super(
        );
        this.destPath = destPath;
    }


    public String getDestpath() {
        return destPath;
    }

    public void setDestpath(String destPath) {
        this.destPath = destPath;
    }


}