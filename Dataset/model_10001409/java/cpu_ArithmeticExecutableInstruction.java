





import java.util.List;
import java.util.ArrayList;

public class cpu_ArithmeticExecutableInstruction  {

    private int s2;
    private int d;
    private int s1;



    public cpu_ArithmeticExecutableInstruction(
        int s2,        int d,        int s1    ) {
        this.s2 = s2;
        this.d = d;
        this.s1 = s1;
    }


    public int getS2() {
        return s2;
    }

    public void setS2(int s2) {
        this.s2 = s2;
    }
    public int getD() {
        return d;
    }

    public void setD(int d) {
        this.d = d;
    }
    public int getS1() {
        return s1;
    }

    public void setS1(int s1) {
        this.s1 = s1;
    }


}