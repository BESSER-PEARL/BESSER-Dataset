





import java.util.List;
import java.util.ArrayList;

public class C  {

    private boolean att2;
    private int att1;





    private List<B> bs;


    public C(
        boolean att2,        int att1    ) {
        this.att2 = att2;
        this.att1 = att1;
        this.bs = new ArrayList<>();
    }

    public C(
        boolean att2,        int att1        ArrayList<B> bs    ) {
        this.att2 = att2;
        this.att1 = att1;
        this.bs = bs;
    }

    public boolean getAtt2() {
        return att2;
    }

    public void setAtt2(boolean att2) {
        this.att2 = att2;
    }
    public int getAtt1() {
        return att1;
    }

    public void setAtt1(int att1) {
        this.att1 = att1;
    }

    public List<B> getBs() {
        return bs;
    }

    public void addB(B b) {
        this.bs.add(b);
    }

}