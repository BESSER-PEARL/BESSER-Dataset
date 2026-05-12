





import java.util.List;
import java.util.ArrayList;

public class AssociationDataStateBase  {






    private HSM_StateBase hsm_statebase;




    private HSM_DataVar hsm_datavar;


    public AssociationDataStateBase(
    ) {
    }



    public HSM_StateBase getHsm_statebase() {
        return hsm_statebase;
    }

    public void setHsm_statebase(HSM_StateBase hsm_statebase) {
        this.hsm_statebase = hsm_statebase;
    }
    public HSM_DataVar getHsm_datavar() {
        return hsm_datavar;
    }

    public void setHsm_datavar(HSM_DataVar hsm_datavar) {
        this.hsm_datavar = hsm_datavar;
    }

}