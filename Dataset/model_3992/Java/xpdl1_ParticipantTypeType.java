





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ParticipantTypeType  {

    private String type;





    private xpdl1_ParticipantType xpdl1_participanttype;




    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_ParticipantTypeType(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xpdl1_ParticipantType getXpdl1_participanttype() {
        return xpdl1_participanttype;
    }

    public void setXpdl1_participanttype(xpdl1_ParticipantType xpdl1_participanttype) {
        this.xpdl1_participanttype = xpdl1_participanttype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}