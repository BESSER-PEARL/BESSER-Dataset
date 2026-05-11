





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_Resource  {

    private String resMult;
    private String isProtected;
    private String isActive;





    private GRM_MARTE_ConnectableElement grm_marte_connectableelement;


    public MARTE_GRM_Resource(
        String resMult,        String isProtected,        String isActive    ) {
        this.resMult = resMult;
        this.isProtected = isProtected;
        this.isActive = isActive;
    }


    public String getResmult() {
        return resMult;
    }

    public void setResmult(String resMult) {
        this.resMult = resMult;
    }
    public String getIsprotected() {
        return isProtected;
    }

    public void setIsprotected(String isProtected) {
        this.isProtected = isProtected;
    }
    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public GRM_MARTE_ConnectableElement getGrm_marte_connectableelement() {
        return grm_marte_connectableelement;
    }

    public void setGrm_marte_connectableelement(GRM_MARTE_ConnectableElement grm_marte_connectableelement) {
        this.grm_marte_connectableelement = grm_marte_connectableelement;
    }

}