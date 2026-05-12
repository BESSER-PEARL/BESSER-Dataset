





import java.util.List;
import java.util.ArrayList;

public class ClassC  {

    private boolean attC2;
    private int attC1;





    private ClassB classb;


    public ClassC(
        boolean attC2,        int attC1    ) {
        this.attC2 = attC2;
        this.attC1 = attC1;
    }


    public boolean getAttc2() {
        return attC2;
    }

    public void setAttc2(boolean attC2) {
        this.attC2 = attC2;
    }
    public int getAttc1() {
        return attC1;
    }

    public void setAttc1(int attC1) {
        this.attC1 = attC1;
    }

    public ClassB getClassb() {
        return classb;
    }

    public void setClassb(ClassB classb) {
        this.classb = classb;
    }

}