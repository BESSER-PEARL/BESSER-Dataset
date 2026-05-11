





import java.util.List;
import java.util.ArrayList;

public class mid_operator_GenericEndpoint extends ExtendibleElementEndpoint {

    private String metatargetUri;



    public mid_operator_GenericEndpoint(
        String metatargetUri    ) {
        super(
        );
        this.metatargetUri = metatargetUri;
    }


    public String getMetatargeturi() {
        return metatargetUri;
    }

    public void setMetatargeturi(String metatargetUri) {
        this.metatargetUri = metatargetUri;
    }


}