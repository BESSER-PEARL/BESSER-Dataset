





import java.util.List;
import java.util.ArrayList;

public class build_FragmentHost  {






    private List<build_RequiredCapability> build_requiredcapabilitys;




    private build_BuildUnit build_buildunit;


    public build_FragmentHost(
    ) {
        this.build_requiredcapabilitys = new ArrayList<>();
    }

    public build_FragmentHost(
        ArrayList<build_RequiredCapability> build_requiredcapabilitys    ) {
        this.build_requiredcapabilitys = build_requiredcapabilitys;
    }


    public List<build_RequiredCapability> getBuild_requiredcapabilitys() {
        return build_requiredcapabilitys;
    }

    public void addBuild_requiredcapability(Build_requiredcapability build_requiredcapability) {
        this.build_requiredcapabilitys.add(build_requiredcapability);
    }
    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }

}