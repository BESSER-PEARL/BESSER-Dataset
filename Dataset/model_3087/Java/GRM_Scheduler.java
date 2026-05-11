





import java.util.List;
import java.util.ArrayList;

public class GRM_Scheduler  {






    private MARTE_GRM_ProcessingResource marte_grm_processingresource;




    private MARTE_GRM_MutualExclusionResource marte_grm_mutualexclusionresource;




    private MARTE_GRM_SchedulableResource marte_grm_schedulableresource;


    public GRM_Scheduler(
    ) {
    }



    public MARTE_GRM_ProcessingResource getMarte_grm_processingresource() {
        return marte_grm_processingresource;
    }

    public void setMarte_grm_processingresource(MARTE_GRM_ProcessingResource marte_grm_processingresource) {
        this.marte_grm_processingresource = marte_grm_processingresource;
    }
    public MARTE_GRM_MutualExclusionResource getMarte_grm_mutualexclusionresource() {
        return marte_grm_mutualexclusionresource;
    }

    public void setMarte_grm_mutualexclusionresource(MARTE_GRM_MutualExclusionResource marte_grm_mutualexclusionresource) {
        this.marte_grm_mutualexclusionresource = marte_grm_mutualexclusionresource;
    }
    public MARTE_GRM_SchedulableResource getMarte_grm_schedulableresource() {
        return marte_grm_schedulableresource;
    }

    public void setMarte_grm_schedulableresource(MARTE_GRM_SchedulableResource marte_grm_schedulableresource) {
        this.marte_grm_schedulableresource = marte_grm_schedulableresource;
    }

}