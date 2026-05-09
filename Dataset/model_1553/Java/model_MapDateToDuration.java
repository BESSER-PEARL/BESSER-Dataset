




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_MapDateToDuration  {

    private LocalDate key;
    private String value;





    private model_R4EParticipant model_r4eparticipant;


    public model_MapDateToDuration(
        LocalDate key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public LocalDate getKey() {
        return key;
    }

    public void setKey(LocalDate key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public model_R4EParticipant getModel_r4eparticipant() {
        return model_r4eparticipant;
    }

    public void setModel_r4eparticipant(model_R4EParticipant model_r4eparticipant) {
        this.model_r4eparticipant = model_r4eparticipant;
    }

}