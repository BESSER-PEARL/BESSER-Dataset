





import java.util.List;
import java.util.ArrayList;

public class test_EClass2  {

    private int EAttribute1;
    private boolean EAttribute0;





    private test_EClass1 test_eclass1;




    private test_EClass0 test_eclass0;


    public test_EClass2(
        int EAttribute1,        boolean EAttribute0    ) {
        this.EAttribute1 = EAttribute1;
        this.EAttribute0 = EAttribute0;
    }


    public int getEattribute1() {
        return EAttribute1;
    }

    public void setEattribute1(int EAttribute1) {
        this.EAttribute1 = EAttribute1;
    }
    public boolean getEattribute0() {
        return EAttribute0;
    }

    public void setEattribute0(boolean EAttribute0) {
        this.EAttribute0 = EAttribute0;
    }

    public test_EClass1 getTest_eclass1() {
        return test_eclass1;
    }

    public void setTest_eclass1(test_EClass1 test_eclass1) {
        this.test_eclass1 = test_eclass1;
    }
    public test_EClass0 getTest_eclass0() {
        return test_eclass0;
    }

    public void setTest_eclass0(test_EClass0 test_eclass0) {
        this.test_eclass0 = test_eclass0;
    }

}