





import java.util.List;
import java.util.ArrayList;

public class multipleinheritence_NewEClass1 extends NewEClass2, NewEClass3 {

    private int f1;



    public multipleinheritence_NewEClass1(
        int f1    ) {
        super(
        );
        this.f1 = f1;
    }


    public int getF1() {
        return f1;
    }

    public void setF1(int f1) {
        this.f1 = f1;
    }


}