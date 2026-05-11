





import java.util.List;
import java.util.ArrayList;

public class carnot_OrganizationType extends IModelParticipant {






    private carnot_ModelType carnot_modeltype;




    private List<carnot_ParticipantType> carnot_participanttypes;




    private carnot_RoleType carnot_roletype;




    private carnot_OrganizationSymbolType carnot_organizationsymboltype;




    private carnot_RoleType carnot_roletype;




    private List<carnot_OrganizationSymbolType> carnot_organizationsymboltypes;


    public carnot_OrganizationType(
    ) {
        super(
        );
        this.carnot_participanttypes = new ArrayList<>();
        this.carnot_organizationsymboltypes = new ArrayList<>();
    }

    public carnot_OrganizationType(
        ArrayList<carnot_ParticipantType> carnot_participanttypes,        ArrayList<carnot_OrganizationSymbolType> carnot_organizationsymboltypes    ) {
        this.carnot_participanttypes = carnot_participanttypes;
        this.carnot_organizationsymboltypes = carnot_organizationsymboltypes;
    }


    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public List<carnot_ParticipantType> getCarnot_participanttypes() {
        return carnot_participanttypes;
    }

    public void addCarnot_participanttype(Carnot_participanttype carnot_participanttype) {
        this.carnot_participanttypes.add(carnot_participanttype);
    }
    public carnot_RoleType getCarnot_roletype() {
        return carnot_roletype;
    }

    public void setCarnot_roletype(carnot_RoleType carnot_roletype) {
        this.carnot_roletype = carnot_roletype;
    }
    public carnot_OrganizationSymbolType getCarnot_organizationsymboltype() {
        return carnot_organizationsymboltype;
    }

    public void setCarnot_organizationsymboltype(carnot_OrganizationSymbolType carnot_organizationsymboltype) {
        this.carnot_organizationsymboltype = carnot_organizationsymboltype;
    }
    public carnot_RoleType getCarnot_roletype() {
        return carnot_roletype;
    }

    public void setCarnot_roletype(carnot_RoleType carnot_roletype) {
        this.carnot_roletype = carnot_roletype;
    }
    public List<carnot_OrganizationSymbolType> getCarnot_organizationsymboltypes() {
        return carnot_organizationsymboltypes;
    }

    public void addCarnot_organizationsymboltype(Carnot_organizationsymboltype carnot_organizationsymboltype) {
        this.carnot_organizationsymboltypes.add(carnot_organizationsymboltype);
    }

}