





import java.util.List;
import java.util.ArrayList;

public class umm_OclRef  {

    private String name;
    private String multiplicity;





    private umm_OclPathTail umm_oclpathtail;




    private umm_OclPathFeatureHead umm_oclpathfeaturehead;


    public umm_OclRef(
        String name,        String multiplicity    ) {
        this.name = name;
        this.multiplicity = multiplicity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(String multiplicity) {
        this.multiplicity = multiplicity;
    }

    public umm_OclPathTail getUmm_oclpathtail() {
        return umm_oclpathtail;
    }

    public void setUmm_oclpathtail(umm_OclPathTail umm_oclpathtail) {
        this.umm_oclpathtail = umm_oclpathtail;
    }
    public umm_OclPathFeatureHead getUmm_oclpathfeaturehead() {
        return umm_oclpathfeaturehead;
    }

    public void setUmm_oclpathfeaturehead(umm_OclPathFeatureHead umm_oclpathfeaturehead) {
        this.umm_oclpathfeaturehead = umm_oclpathfeaturehead;
    }

}