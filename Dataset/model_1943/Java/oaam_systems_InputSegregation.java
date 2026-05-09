





import java.util.List;
import java.util.ArrayList;

public class oaam_systems_InputSegregation extends OaamBaseElementA {

    private boolean dissimilarSource;
    private boolean dissimilarTechnology;
    private boolean dissimilarRoute;





    private List<RequiredInformationA> requiredinformationas;




    private List<RequiredInformationA> requiredinformationas;


    public oaam_systems_InputSegregation(
        boolean dissimilarSource,        boolean dissimilarTechnology,        boolean dissimilarRoute    ) {
        super(
        );
        this.dissimilarSource = dissimilarSource;
        this.dissimilarTechnology = dissimilarTechnology;
        this.dissimilarRoute = dissimilarRoute;
        this.requiredinformationas = new ArrayList<>();
        this.requiredinformationas = new ArrayList<>();
    }

    public oaam_systems_InputSegregation(
        boolean dissimilarSource,        boolean dissimilarTechnology,        boolean dissimilarRoute        ArrayList<RequiredInformationA> requiredinformationas,        ArrayList<RequiredInformationA> requiredinformationas    ) {
        this.dissimilarSource = dissimilarSource;
        this.dissimilarTechnology = dissimilarTechnology;
        this.dissimilarRoute = dissimilarRoute;
        this.requiredinformationas = requiredinformationas;
        this.requiredinformationas = requiredinformationas;
    }

    public boolean getDissimilarsource() {
        return dissimilarSource;
    }

    public void setDissimilarsource(boolean dissimilarSource) {
        this.dissimilarSource = dissimilarSource;
    }
    public boolean getDissimilartechnology() {
        return dissimilarTechnology;
    }

    public void setDissimilartechnology(boolean dissimilarTechnology) {
        this.dissimilarTechnology = dissimilarTechnology;
    }
    public boolean getDissimilarroute() {
        return dissimilarRoute;
    }

    public void setDissimilarroute(boolean dissimilarRoute) {
        this.dissimilarRoute = dissimilarRoute;
    }

    public List<RequiredInformationA> getRequiredinformationas() {
        return requiredinformationas;
    }

    public void addRequiredinformationa(Requiredinformationa requiredinformationa) {
        this.requiredinformationas.add(requiredinformationa);
    }
    public List<RequiredInformationA> getRequiredinformationas() {
        return requiredinformationas;
    }

    public void addRequiredinformationa(Requiredinformationa requiredinformationa) {
        this.requiredinformationas.add(requiredinformationa);
    }

}