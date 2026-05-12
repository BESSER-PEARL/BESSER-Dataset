





import java.util.List;
import java.util.ArrayList;

public class ecoreTest_EClass2  {

    private String eAttribute3;
    private String eAttribute4;





    private ecoreTest_Eclass1 ecoretest_eclass1;


    public ecoreTest_EClass2(
        String eAttribute3,        String eAttribute4    ) {
        this.eAttribute3 = eAttribute3;
        this.eAttribute4 = eAttribute4;
    }


    public String getEattribute3() {
        return eAttribute3;
    }

    public void setEattribute3(String eAttribute3) {
        this.eAttribute3 = eAttribute3;
    }
    public String getEattribute4() {
        return eAttribute4;
    }

    public void setEattribute4(String eAttribute4) {
        this.eAttribute4 = eAttribute4;
    }

    public ecoreTest_Eclass1 getEcoretest_eclass1() {
        return ecoretest_eclass1;
    }

    public void setEcoretest_eclass1(ecoreTest_Eclass1 ecoretest_eclass1) {
        this.ecoretest_eclass1 = ecoretest_eclass1;
    }

}