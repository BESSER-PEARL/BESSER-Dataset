





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_ServiceEffectSpecification  {

    private String seffTypeID;





    private Signature signature;


    public pcm_seff_ServiceEffectSpecification(
        String seffTypeID    ) {
        this.seffTypeID = seffTypeID;
    }


    public String getSefftypeid() {
        return seffTypeID;
    }

    public void setSefftypeid(String seffTypeID) {
        this.seffTypeID = seffTypeID;
    }

    public Signature getSignature() {
        return signature;
    }

    public void setSignature(Signature signature) {
        this.signature = signature;
    }

}