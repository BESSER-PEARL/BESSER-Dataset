





import java.util.List;
import java.util.ArrayList;

public class shr5_Sichtverhaeltnisse extends ModifikatorAttribute {

    private String restlichtverstaerkung;
    private String infrarot;
    private String ultrasound;



    public shr5_Sichtverhaeltnisse(
        String restlichtverstaerkung,        String infrarot,        String ultrasound    ) {
        super(
        );
        this.restlichtverstaerkung = restlichtverstaerkung;
        this.infrarot = infrarot;
        this.ultrasound = ultrasound;
    }


    public String getRestlichtverstaerkung() {
        return restlichtverstaerkung;
    }

    public void setRestlichtverstaerkung(String restlichtverstaerkung) {
        this.restlichtverstaerkung = restlichtverstaerkung;
    }
    public String getInfrarot() {
        return infrarot;
    }

    public void setInfrarot(String infrarot) {
        this.infrarot = infrarot;
    }
    public String getUltrasound() {
        return ultrasound;
    }

    public void setUltrasound(String ultrasound) {
        this.ultrasound = ultrasound;
    }


}