





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_seff_av_pc_ServiceEffectSpecification  {

    private String seffTypeID;





    private BasicComponent basiccomponent;




    private Signature signature;


    public pcm_av_pc_seff_av_pc_ServiceEffectSpecification(
        String seffTypeID    ) {
        this.seffTypeID = seffTypeID;
    }


    public String getSefftypeid() {
        return seffTypeID;
    }

    public void setSefftypeid(String seffTypeID) {
        this.seffTypeID = seffTypeID;
    }

    public BasicComponent getBasiccomponent() {
        return basiccomponent;
    }

    public void setBasiccomponent(BasicComponent basiccomponent) {
        this.basiccomponent = basiccomponent;
    }
    public Signature getSignature() {
        return signature;
    }

    public void setSignature(Signature signature) {
        this.signature = signature;
    }

}