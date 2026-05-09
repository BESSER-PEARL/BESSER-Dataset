





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place extends PetriElement {

    private String borne;
    private String nbJeton;



    public PetriNet_Place(
        String borne,        String nbJeton    ) {
        super(
        );
        this.borne = borne;
        this.nbJeton = nbJeton;
    }


    public String getBorne() {
        return borne;
    }

    public void setBorne(String borne) {
        this.borne = borne;
    }
    public String getNbjeton() {
        return nbJeton;
    }

    public void setNbjeton(String nbJeton) {
        this.nbJeton = nbJeton;
    }


}