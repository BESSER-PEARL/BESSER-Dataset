





import java.util.List;
import java.util.ArrayList;

public class testModel_upperBoundLeaf extends Leafs {

    private String name;





    private testModel_ContainedLeaf testmodel_containedleaf;


    public testModel_upperBoundLeaf(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public testModel_ContainedLeaf getTestmodel_containedleaf() {
        return testmodel_containedleaf;
    }

    public void setTestmodel_containedleaf(testModel_ContainedLeaf testmodel_containedleaf) {
        this.testmodel_containedleaf = testmodel_containedleaf;
    }

}