





import java.util.List;
import java.util.ArrayList;

public class NBVR_Grammar_DomainForm extends Sentence {

    private String modality;



    public NBVR_Grammar_DomainForm(
        String modality    ) {
        super(
        );
        this.modality = modality;
    }


    public String getModality() {
        return modality;
    }

    public void setModality(String modality) {
        this.modality = modality;
    }


}