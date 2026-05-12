





import java.util.List;
import java.util.ArrayList;

public class courses  {

    private String c_name;
    private int cid;





    private List<Tescher> teschers;


    public courses(
        String c_name,        int cid    ) {
        this.c_name = c_name;
        this.cid = cid;
        this.teschers = new ArrayList<>();
    }

    public courses(
        String c_name,        int cid        ArrayList<Tescher> teschers    ) {
        this.c_name = c_name;
        this.cid = cid;
        this.teschers = teschers;
    }

    public String getC_name() {
        return c_name;
    }

    public void setC_name(String c_name) {
        this.c_name = c_name;
    }
    public int getCid() {
        return cid;
    }

    public void setCid(int cid) {
        this.cid = cid;
    }

    public List<Tescher> getTeschers() {
        return teschers;
    }

    public void addTescher(Tescher tescher) {
        this.teschers.add(tescher);
    }

}