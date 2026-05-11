





import java.util.List;
import java.util.ArrayList;

public class testModel_multiRefElement extends Element {

    private String name;





    private testModel_referenziertesElement testmodel_referenzierteselement;


    public testModel_multiRefElement(
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

    public testModel_referenziertesElement getTestmodel_referenzierteselement() {
        return testmodel_referenzierteselement;
    }

    public void setTestmodel_referenzierteselement(testModel_referenziertesElement testmodel_referenzierteselement) {
        this.testmodel_referenzierteselement = testmodel_referenzierteselement;
    }

}