





import java.util.List;
import java.util.ArrayList;

public class builderState_ReferenceDescription extends IReferenceDescription {

    private String externalFormOfEReference;



    public builderState_ReferenceDescription(
        String externalFormOfEReference    ) {
        super(
        );
        this.externalFormOfEReference = externalFormOfEReference;
    }


    public String getExternalformofereference() {
        return externalFormOfEReference;
    }

    public void setExternalformofereference(String externalFormOfEReference) {
        this.externalFormOfEReference = externalFormOfEReference;
    }


}