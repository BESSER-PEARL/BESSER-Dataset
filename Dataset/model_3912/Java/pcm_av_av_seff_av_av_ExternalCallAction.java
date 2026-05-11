





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_seff_av_av_ExternalCallAction extends seff_reliability_av_av_FailureHandlingEntity, seff_av_av_AbstractAction, seff_av_av_CallReturnAction {

    private int retryCount;



    public pcm_av_av_seff_av_av_ExternalCallAction(
        int retryCount    ) {
        super(
        );
        this.retryCount = retryCount;
    }


    public int getRetrycount() {
        return retryCount;
    }

    public void setRetrycount(int retryCount) {
        this.retryCount = retryCount;
    }


}