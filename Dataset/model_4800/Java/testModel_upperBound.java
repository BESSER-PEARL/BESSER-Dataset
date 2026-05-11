





import java.util.List;
import java.util.ArrayList;

public class testModel_upperBound extends Element {

    private String name;





    private testModel_ContainedElement testmodel_containedelement;


    public testModel_upperBound(
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

    public testModel_ContainedElement getTestmodel_containedelement() {
        return testmodel_containedelement;
    }

    public void setTestmodel_containedelement(testModel_ContainedElement testmodel_containedelement) {
        this.testmodel_containedelement = testmodel_containedelement;
    }

}