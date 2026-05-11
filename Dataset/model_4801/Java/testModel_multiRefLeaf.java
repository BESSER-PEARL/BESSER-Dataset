





import java.util.List;
import java.util.ArrayList;

public class testModel_multiRefLeaf extends Leafs {

    private String name;





    private testModel_referedLeaf testmodel_referedleaf;


    public testModel_multiRefLeaf(
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

    public testModel_referedLeaf getTestmodel_referedleaf() {
        return testmodel_referedleaf;
    }

    public void setTestmodel_referedleaf(testModel_referedLeaf testmodel_referedleaf) {
        this.testmodel_referedleaf = testmodel_referedleaf;
    }

}