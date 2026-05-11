





import java.util.List;
import java.util.ArrayList;

public class testModel_BClass extends AClass {

    private String BClassAttr2;
    private boolean BClassAttr1;





    private testModel_AClass testmodel_aclass;


    public testModel_BClass(
        String BClassAttr2,        boolean BClassAttr1    ) {
        super(
        );
        this.BClassAttr2 = BClassAttr2;
        this.BClassAttr1 = BClassAttr1;
    }


    public String getBclassattr2() {
        return BClassAttr2;
    }

    public void setBclassattr2(String BClassAttr2) {
        this.BClassAttr2 = BClassAttr2;
    }
    public boolean getBclassattr1() {
        return BClassAttr1;
    }

    public void setBclassattr1(boolean BClassAttr1) {
        this.BClassAttr1 = BClassAttr1;
    }

    public testModel_AClass getTestmodel_aclass() {
        return testmodel_aclass;
    }

    public void setTestmodel_aclass(testModel_AClass testmodel_aclass) {
        this.testmodel_aclass = testmodel_aclass;
    }

}