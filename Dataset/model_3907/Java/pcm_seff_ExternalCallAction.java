





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_ExternalCallAction extends AbstractAction {

    private int retryCount;



    public pcm_seff_ExternalCallAction(
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