





import java.util.List;
import java.util.ArrayList;

public class model_R4EID  {

    private int sequenceID;
    private String userID;





    private model_R4EIDComponent model_r4eidcomponent;




    private model_MapIDToComponent model_mapidtocomponent;




    private model_R4EParticipant model_r4eparticipant;


    public model_R4EID(
        int sequenceID,        String userID    ) {
        this.sequenceID = sequenceID;
        this.userID = userID;
    }


    public int getSequenceid() {
        return sequenceID;
    }

    public void setSequenceid(int sequenceID) {
        this.sequenceID = sequenceID;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }

    public model_R4EIDComponent getModel_r4eidcomponent() {
        return model_r4eidcomponent;
    }

    public void setModel_r4eidcomponent(model_R4EIDComponent model_r4eidcomponent) {
        this.model_r4eidcomponent = model_r4eidcomponent;
    }
    public model_MapIDToComponent getModel_mapidtocomponent() {
        return model_mapidtocomponent;
    }

    public void setModel_mapidtocomponent(model_MapIDToComponent model_mapidtocomponent) {
        this.model_mapidtocomponent = model_mapidtocomponent;
    }
    public model_R4EParticipant getModel_r4eparticipant() {
        return model_r4eparticipant;
    }

    public void setModel_r4eparticipant(model_R4EParticipant model_r4eparticipant) {
        this.model_r4eparticipant = model_r4eparticipant;
    }

}