





import java.util.List;
import java.util.ArrayList;

public class build_BeeModel extends BChainedExpression, IBuildUnitContainer {






    private List<build_BPropertySet> build_bpropertysets;




    private List<build_IType> build_itypes;




    private List<build_Repository> build_repositorys;




    private List<build_BConcern> build_bconcerns;




    private List<build_FirstFoundUnitProvider> build_firstfoundunitproviders;




    private build_BeeHive build_beehive;




    private build_BPropertySet build_bpropertyset;


    public build_BeeModel(
    ) {
        super(
        );
        this.build_bpropertysets = new ArrayList<>();
        this.build_itypes = new ArrayList<>();
        this.build_repositorys = new ArrayList<>();
        this.build_bconcerns = new ArrayList<>();
        this.build_firstfoundunitproviders = new ArrayList<>();
    }

    public build_BeeModel(
        ArrayList<build_BPropertySet> build_bpropertysets,        ArrayList<build_IType> build_itypes,        ArrayList<build_Repository> build_repositorys,        ArrayList<build_BConcern> build_bconcerns,        ArrayList<build_FirstFoundUnitProvider> build_firstfoundunitproviders    ) {
        this.build_bpropertysets = build_bpropertysets;
        this.build_itypes = build_itypes;
        this.build_repositorys = build_repositorys;
        this.build_bconcerns = build_bconcerns;
        this.build_firstfoundunitproviders = build_firstfoundunitproviders;
    }


    public List<build_BPropertySet> getBuild_bpropertysets() {
        return build_bpropertysets;
    }

    public void addBuild_bpropertyset(Build_bpropertyset build_bpropertyset) {
        this.build_bpropertysets.add(build_bpropertyset);
    }
    public List<build_IType> getBuild_itypes() {
        return build_itypes;
    }

    public void addBuild_itype(Build_itype build_itype) {
        this.build_itypes.add(build_itype);
    }
    public List<build_Repository> getBuild_repositorys() {
        return build_repositorys;
    }

    public void addBuild_repository(Build_repository build_repository) {
        this.build_repositorys.add(build_repository);
    }
    public List<build_BConcern> getBuild_bconcerns() {
        return build_bconcerns;
    }

    public void addBuild_bconcern(Build_bconcern build_bconcern) {
        this.build_bconcerns.add(build_bconcern);
    }
    public List<build_FirstFoundUnitProvider> getBuild_firstfoundunitproviders() {
        return build_firstfoundunitproviders;
    }

    public void addBuild_firstfoundunitprovider(Build_firstfoundunitprovider build_firstfoundunitprovider) {
        this.build_firstfoundunitproviders.add(build_firstfoundunitprovider);
    }
    public build_BeeHive getBuild_beehive() {
        return build_beehive;
    }

    public void setBuild_beehive(build_BeeHive build_beehive) {
        this.build_beehive = build_beehive;
    }
    public build_BPropertySet getBuild_bpropertyset() {
        return build_bpropertyset;
    }

    public void setBuild_bpropertyset(build_BPropertySet build_bpropertyset) {
        this.build_bpropertyset = build_bpropertyset;
    }

}