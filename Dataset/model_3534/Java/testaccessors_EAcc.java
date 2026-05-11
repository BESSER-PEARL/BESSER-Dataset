





import java.util.List;
import java.util.ArrayList;

public class testaccessors_EAcc  {

    private boolean b;
    private int i;
    private boolean bs;
    private int is_;



    public testaccessors_EAcc(
        boolean b,        int i,        boolean bs,        int is_    ) {
        this.b = b;
        this.i = i;
        this.bs = bs;
        this.is_ = is_;
    }


    public boolean getB() {
        return b;
    }

    public void setB(boolean b) {
        this.b = b;
    }
    public int getI() {
        return i;
    }

    public void setI(int i) {
        this.i = i;
    }
    public boolean getBs() {
        return bs;
    }

    public void setBs(boolean bs) {
        this.bs = bs;
    }
    public int getIs_() {
        return is_;
    }

    public void setIs_(int is_) {
        this.is_ = is_;
    }


}