





import java.util.List;
import java.util.ArrayList;

public class featureModel_Project  {

    private boolean validatedTEF;
    private boolean validatedOCL;
    private int numberOfProducts;
    private String nameConstraintsFile;
    private String nameConfigFile;





    private List<featureModel_Node> featuremodel_nodes;


    public featureModel_Project(
        boolean validatedTEF,        boolean validatedOCL,        int numberOfProducts,        String nameConstraintsFile,        String nameConfigFile    ) {
        this.validatedTEF = validatedTEF;
        this.validatedOCL = validatedOCL;
        this.numberOfProducts = numberOfProducts;
        this.nameConstraintsFile = nameConstraintsFile;
        this.nameConfigFile = nameConfigFile;
        this.featuremodel_nodes = new ArrayList<>();
    }

    public featureModel_Project(
        boolean validatedTEF,        boolean validatedOCL,        int numberOfProducts,        String nameConstraintsFile,        String nameConfigFile        ArrayList<featureModel_Node> featuremodel_nodes    ) {
        this.validatedTEF = validatedTEF;
        this.validatedOCL = validatedOCL;
        this.numberOfProducts = numberOfProducts;
        this.nameConstraintsFile = nameConstraintsFile;
        this.nameConfigFile = nameConfigFile;
        this.featuremodel_nodes = featuremodel_nodes;
    }

    public boolean getValidatedtef() {
        return validatedTEF;
    }

    public void setValidatedtef(boolean validatedTEF) {
        this.validatedTEF = validatedTEF;
    }
    public boolean getValidatedocl() {
        return validatedOCL;
    }

    public void setValidatedocl(boolean validatedOCL) {
        this.validatedOCL = validatedOCL;
    }
    public int getNumberofproducts() {
        return numberOfProducts;
    }

    public void setNumberofproducts(int numberOfProducts) {
        this.numberOfProducts = numberOfProducts;
    }
    public String getNameconstraintsfile() {
        return nameConstraintsFile;
    }

    public void setNameconstraintsfile(String nameConstraintsFile) {
        this.nameConstraintsFile = nameConstraintsFile;
    }
    public String getNameconfigfile() {
        return nameConfigFile;
    }

    public void setNameconfigfile(String nameConfigFile) {
        this.nameConfigFile = nameConfigFile;
    }

    public List<featureModel_Node> getFeaturemodel_nodes() {
        return featuremodel_nodes;
    }

    public void addFeaturemodel_node(Featuremodel_node featuremodel_node) {
        this.featuremodel_nodes.add(featuremodel_node);
    }

}