





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_Pilot extends Crew {

    private String certificationId;
    private int experience;



    public reservationsystem_Pilot(
        String certificationId,        int experience    ) {
        super(
        );
        this.certificationId = certificationId;
        this.experience = experience;
    }


    public String getCertificationid() {
        return certificationId;
    }

    public void setCertificationid(String certificationId) {
        this.certificationId = certificationId;
    }
    public int getExperience() {
        return experience;
    }

    public void setExperience(int experience) {
        this.experience = experience;
    }


}