





import java.util.List;
import java.util.ArrayList;

public class specializationModel_Project  {

    private String featureModelURI;
    private boolean infiniteDomain;
    private boolean userConstraintsState;
    private int numberOfProducts;
    private String nameConfigFile;
    private String nameConstraintsFile;



    public specializationModel_Project(
        String featureModelURI,        boolean infiniteDomain,        boolean userConstraintsState,        int numberOfProducts,        String nameConfigFile,        String nameConstraintsFile    ) {
        this.featureModelURI = featureModelURI;
        this.infiniteDomain = infiniteDomain;
        this.userConstraintsState = userConstraintsState;
        this.numberOfProducts = numberOfProducts;
        this.nameConfigFile = nameConfigFile;
        this.nameConstraintsFile = nameConstraintsFile;
    }


    public String getFeaturemodeluri() {
        return featureModelURI;
    }

    public void setFeaturemodeluri(String featureModelURI) {
        this.featureModelURI = featureModelURI;
    }
    public boolean getInfinitedomain() {
        return infiniteDomain;
    }

    public void setInfinitedomain(boolean infiniteDomain) {
        this.infiniteDomain = infiniteDomain;
    }
    public boolean getUserconstraintsstate() {
        return userConstraintsState;
    }

    public void setUserconstraintsstate(boolean userConstraintsState) {
        this.userConstraintsState = userConstraintsState;
    }
    public int getNumberofproducts() {
        return numberOfProducts;
    }

    public void setNumberofproducts(int numberOfProducts) {
        this.numberOfProducts = numberOfProducts;
    }
    public String getNameconfigfile() {
        return nameConfigFile;
    }

    public void setNameconfigfile(String nameConfigFile) {
        this.nameConfigFile = nameConfigFile;
    }
    public String getNameconstraintsfile() {
        return nameConstraintsFile;
    }

    public void setNameconstraintsfile(String nameConstraintsFile) {
        this.nameConstraintsFile = nameConstraintsFile;
    }


}