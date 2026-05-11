





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_seff_pc_av_ServiceEffectSpecification  {

    private String seffTypeID;





    private BasicComponent basiccomponent;


    public pcm_pc_av_seff_pc_av_ServiceEffectSpecification(
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

}