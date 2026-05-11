





import java.util.List;
import java.util.ArrayList;

public class pimm_ConfigOutputPort extends DataOutputPort, ISetter {






    private pimm_AbstractActor pimm_abstractactor;


    public pimm_ConfigOutputPort(
    ) {
        super(
        );
    }



    public pimm_AbstractActor getPimm_abstractactor() {
        return pimm_abstractactor;
    }

    public void setPimm_abstractactor(pimm_AbstractActor pimm_abstractactor) {
        this.pimm_abstractactor = pimm_abstractactor;
    }

}