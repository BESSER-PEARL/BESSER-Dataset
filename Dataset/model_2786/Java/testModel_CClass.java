





import java.util.List;
import java.util.ArrayList;

public class testModel_CClass extends BClass {

    private boolean CClassAttr1;
    private String CClassAttr2;





    private testModel_BClass testmodel_bclass;


    public testModel_CClass(
        boolean CClassAttr1,        String CClassAttr2    ) {
        super(
        );
        this.CClassAttr1 = CClassAttr1;
        this.CClassAttr2 = CClassAttr2;
    }


    public boolean getCclassattr1() {
        return CClassAttr1;
    }

    public void setCclassattr1(boolean CClassAttr1) {
        this.CClassAttr1 = CClassAttr1;
    }
    public String getCclassattr2() {
        return CClassAttr2;
    }

    public void setCclassattr2(String CClassAttr2) {
        this.CClassAttr2 = CClassAttr2;
    }

    public testModel_BClass getTestmodel_bclass() {
        return testmodel_bclass;
    }

    public void setTestmodel_bclass(testModel_BClass testmodel_bclass) {
        this.testmodel_bclass = testmodel_bclass;
    }

}