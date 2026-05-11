





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_ResourceCore_SwAccessService extends GrService {

    private String isModifier;



    public MARTE_SW_ResourceCore_SwAccessService(
        String isModifier    ) {
        super(
        );
        this.isModifier = isModifier;
    }


    public String getIsmodifier() {
        return isModifier;
    }

    public void setIsmodifier(String isModifier) {
        this.isModifier = isModifier;
    }


}