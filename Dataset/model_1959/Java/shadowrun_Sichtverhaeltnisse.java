





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Sichtverhaeltnisse  {

    private String Ultrasound;
    private String Restlichtverstaerkung;
    private String Infrarot;



    public shadowrun_Sichtverhaeltnisse(
        String Ultrasound,        String Restlichtverstaerkung,        String Infrarot    ) {
        this.Ultrasound = Ultrasound;
        this.Restlichtverstaerkung = Restlichtverstaerkung;
        this.Infrarot = Infrarot;
    }


    public String getUltrasound() {
        return Ultrasound;
    }

    public void setUltrasound(String Ultrasound) {
        this.Ultrasound = Ultrasound;
    }
    public String getRestlichtverstaerkung() {
        return Restlichtverstaerkung;
    }

    public void setRestlichtverstaerkung(String Restlichtverstaerkung) {
        this.Restlichtverstaerkung = Restlichtverstaerkung;
    }
    public String getInfrarot() {
        return Infrarot;
    }

    public void setInfrarot(String Infrarot) {
        this.Infrarot = Infrarot;
    }


}