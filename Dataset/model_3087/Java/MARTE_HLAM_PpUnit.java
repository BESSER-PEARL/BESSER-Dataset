





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_PpUnit  {

    private String concPolicy;





    private NFP_DataSize nfp_datasize;




    private HLAM_MARTE_BehavioredClassifier hlam_marte_behavioredclassifier;


    public MARTE_HLAM_PpUnit(
        String concPolicy    ) {
        this.concPolicy = concPolicy;
    }


    public String getConcpolicy() {
        return concPolicy;
    }

    public void setConcpolicy(String concPolicy) {
        this.concPolicy = concPolicy;
    }

    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }
    public HLAM_MARTE_BehavioredClassifier getHlam_marte_behavioredclassifier() {
        return hlam_marte_behavioredclassifier;
    }

    public void setHlam_marte_behavioredclassifier(HLAM_MARTE_BehavioredClassifier hlam_marte_behavioredclassifier) {
        this.hlam_marte_behavioredclassifier = hlam_marte_behavioredclassifier;
    }

}