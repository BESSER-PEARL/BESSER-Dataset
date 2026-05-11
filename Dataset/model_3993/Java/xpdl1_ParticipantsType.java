





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ParticipantsType  {






    private xpdl1_PackageType xpdl1_packagetype;




    private xpdl1_DocumentRoot xpdl1_documentroot;




    private List<xpdl1_ParticipantType> xpdl1_participanttypes;


    public xpdl1_ParticipantsType(
    ) {
        this.xpdl1_participanttypes = new ArrayList<>();
    }

    public xpdl1_ParticipantsType(
        ArrayList<xpdl1_ParticipantType> xpdl1_participanttypes    ) {
        this.xpdl1_participanttypes = xpdl1_participanttypes;
    }


    public xpdl1_PackageType getXpdl1_packagetype() {
        return xpdl1_packagetype;
    }

    public void setXpdl1_packagetype(xpdl1_PackageType xpdl1_packagetype) {
        this.xpdl1_packagetype = xpdl1_packagetype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public List<xpdl1_ParticipantType> getXpdl1_participanttypes() {
        return xpdl1_participanttypes;
    }

    public void addXpdl1_participanttype(Xpdl1_participanttype xpdl1_participanttype) {
        this.xpdl1_participanttypes.add(xpdl1_participanttype);
    }

}