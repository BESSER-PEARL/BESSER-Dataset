





import java.util.List;
import java.util.ArrayList;

public class builds_BuildModel  {






    private List<builds_BuildServer> builds_buildservers;




    private List<builds_Build> builds_builds;




    private List<builds_BuildPlan> builds_buildplans;


    public builds_BuildModel(
    ) {
        this.builds_buildservers = new ArrayList<>();
        this.builds_builds = new ArrayList<>();
        this.builds_buildplans = new ArrayList<>();
    }

    public builds_BuildModel(
        ArrayList<builds_BuildServer> builds_buildservers,        ArrayList<builds_Build> builds_builds,        ArrayList<builds_BuildPlan> builds_buildplans    ) {
        this.builds_buildservers = builds_buildservers;
        this.builds_builds = builds_builds;
        this.builds_buildplans = builds_buildplans;
    }


    public List<builds_BuildServer> getBuilds_buildservers() {
        return builds_buildservers;
    }

    public void addBuilds_buildserver(Builds_buildserver builds_buildserver) {
        this.builds_buildservers.add(builds_buildserver);
    }
    public List<builds_Build> getBuilds_builds() {
        return builds_builds;
    }

    public void addBuilds_build(Builds_build builds_build) {
        this.builds_builds.add(builds_build);
    }
    public List<builds_BuildPlan> getBuilds_buildplans() {
        return builds_buildplans;
    }

    public void addBuilds_buildplan(Builds_buildplan builds_buildplan) {
        this.builds_buildplans.add(builds_buildplan);
    }

}