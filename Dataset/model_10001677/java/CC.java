





import java.util.List;
import java.util.ArrayList;

public class CC  {

    private boolean attC2;
    private int attC1;





    private BB bb;


    public CC(
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

    public BB getBb() {
        return bb;
    }

    public void setBb(BB bb) {
        this.bb = bb;
    }

}