





import java.util.List;
import java.util.ArrayList;

public class build_IArtifactsPart extends IBuildPart {






    private List<build_IPathGroup> build_ipathgroups;


    public build_IArtifactsPart(
    ) {
        super(
        );
        this.build_ipathgroups = new ArrayList<>();
    }

    public build_IArtifactsPart(
        ArrayList<build_IPathGroup> build_ipathgroups    ) {
        this.build_ipathgroups = build_ipathgroups;
    }


    public List<build_IPathGroup> getBuild_ipathgroups() {
        return build_ipathgroups;
    }

    public void addBuild_ipathgroup(Build_ipathgroup build_ipathgroup) {
        this.build_ipathgroups.add(build_ipathgroup);
    }

}