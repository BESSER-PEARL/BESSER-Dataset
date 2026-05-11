





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_seff_pc_ServiceEffectSpecification  {

    private String seffTypeID;





    private Signature signature;




    private BasicComponent basiccomponent;


    public pcm_pc_seff_pc_ServiceEffectSpecification(
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
    public BasicComponent getBasiccomponent() {
        return basiccomponent;
    }

    public void setBasiccomponent(BasicComponent basiccomponent) {
        this.basiccomponent = basiccomponent;
    }

}