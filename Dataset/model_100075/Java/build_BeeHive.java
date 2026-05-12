





import java.util.List;
import java.util.ArrayList;

public class build_BeeHive  {

    private String resolutions;





    private List<build_BeeModel> build_beemodels;




    private build_BeeHive build_beehive;


    public build_BeeHive(
        String resolutions    ) {
        this.resolutions = resolutions;
        this.build_beemodels = new ArrayList<>();
    }

    public build_BeeHive(
        String resolutions        ArrayList<build_BeeModel> build_beemodels    ) {
        this.resolutions = resolutions;
        this.build_beemodels = build_beemodels;
    }

    public String getResolutions() {
        return resolutions;
    }

    public void setResolutions(String resolutions) {
        this.resolutions = resolutions;
    }

    public List<build_BeeModel> getBuild_beemodels() {
        return build_beemodels;
    }

    public void addBuild_beemodel(Build_beemodel build_beemodel) {
        this.build_beemodels.add(build_beemodel);
    }
    public build_BeeHive getBuild_beehive() {
        return build_beehive;
    }

    public void setBuild_beehive(build_BeeHive build_beehive) {
        this.build_beehive = build_beehive;
    }

}