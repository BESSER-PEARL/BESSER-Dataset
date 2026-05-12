





import java.util.List;
import java.util.ArrayList;

public class HAL_AutreType extends ReferenceBiblioType {

    private String annee;
    private String urldoi;
    private String description;



    public HAL_AutreType(
        String annee,        String urldoi,        String description    ) {
        super(
        );
        this.annee = annee;
        this.urldoi = urldoi;
        this.description = description;
    }


    public String getAnnee() {
        return annee;
    }

    public void setAnnee(String annee) {
        this.annee = annee;
    }
    public String getUrldoi() {
        return urldoi;
    }

    public void setUrldoi(String urldoi) {
        this.urldoi = urldoi;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}