





import java.util.List;
import java.util.ArrayList;

public class reqSpec_RequirementSet extends ReqRoot {






    private List<reqSpec_ReqRoot> reqspec_reqroots;




    private List<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations;




    private List<reqSpec_GlobalConstants> reqspec_globalconstantss;




    private List<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations;


    public reqSpec_RequirementSet(
    ) {
        super(
        );
        this.reqspec_reqroots = new ArrayList<>();
        this.reqspec_avariabledeclarations = new ArrayList<>();
        this.reqspec_globalconstantss = new ArrayList<>();
        this.reqspec_avariabledeclarations = new ArrayList<>();
    }

    public reqSpec_RequirementSet(
        ArrayList<reqSpec_ReqRoot> reqspec_reqroots,        ArrayList<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations,        ArrayList<reqSpec_GlobalConstants> reqspec_globalconstantss,        ArrayList<reqSpec_AVariableDeclaration> reqspec_avariabledeclarations    ) {
        this.reqspec_reqroots = reqspec_reqroots;
        this.reqspec_avariabledeclarations = reqspec_avariabledeclarations;
        this.reqspec_globalconstantss = reqspec_globalconstantss;
        this.reqspec_avariabledeclarations = reqspec_avariabledeclarations;
    }


    public List<reqSpec_ReqRoot> getReqspec_reqroots() {
        return reqspec_reqroots;
    }

    public void addReqspec_reqroot(Reqspec_reqroot reqspec_reqroot) {
        this.reqspec_reqroots.add(reqspec_reqroot);
    }
    public List<reqSpec_AVariableDeclaration> getReqspec_avariabledeclarations() {
        return reqspec_avariabledeclarations;
    }

    public void addReqspec_avariabledeclaration(Reqspec_avariabledeclaration reqspec_avariabledeclaration) {
        this.reqspec_avariabledeclarations.add(reqspec_avariabledeclaration);
    }
    public List<reqSpec_GlobalConstants> getReqspec_globalconstantss() {
        return reqspec_globalconstantss;
    }

    public void addReqspec_globalconstants(Reqspec_globalconstants reqspec_globalconstants) {
        this.reqspec_globalconstantss.add(reqspec_globalconstants);
    }
    public List<reqSpec_AVariableDeclaration> getReqspec_avariabledeclarations() {
        return reqspec_avariabledeclarations;
    }

    public void addReqspec_avariabledeclaration(Reqspec_avariabledeclaration reqspec_avariabledeclaration) {
        this.reqspec_avariabledeclarations.add(reqspec_avariabledeclaration);
    }

}