





import java.util.List;
import java.util.ArrayList;

public class pgohttpestest_B  {

    private int priv1;





    private List<pgohttpestest_C> pgohttpestest_cs;




    private pgohttpestest_Root pgohttpestest_root;


    public pgohttpestest_B(
        int priv1    ) {
        this.priv1 = priv1;
        this.pgohttpestest_cs = new ArrayList<>();
    }

    public pgohttpestest_B(
        int priv1        ArrayList<pgohttpestest_C> pgohttpestest_cs    ) {
        this.priv1 = priv1;
        this.pgohttpestest_cs = pgohttpestest_cs;
    }

    public int getPriv1() {
        return priv1;
    }

    public void setPriv1(int priv1) {
        this.priv1 = priv1;
    }

    public List<pgohttpestest_C> getPgohttpestest_cs() {
        return pgohttpestest_cs;
    }

    public void addPgohttpestest_c(Pgohttpestest_c pgohttpestest_c) {
        this.pgohttpestest_cs.add(pgohttpestest_c);
    }
    public pgohttpestest_Root getPgohttpestest_root() {
        return pgohttpestest_root;
    }

    public void setPgohttpestest_root(pgohttpestest_Root pgohttpestest_root) {
        this.pgohttpestest_root = pgohttpestest_root;
    }

}