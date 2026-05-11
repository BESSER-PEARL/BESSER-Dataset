





import java.util.List;
import java.util.ArrayList;

public class myffbd_Function extends SequenceNode {

    private int tMin;
    private String domain;
    private int tMax;





    private List<myffbd_Function> myffbd_functions;


    public myffbd_Function(
        int tMin,        String domain,        int tMax    ) {
        super(
        );
        this.tMin = tMin;
        this.domain = domain;
        this.tMax = tMax;
        this.myffbd_functions = new ArrayList<>();
    }

    public myffbd_Function(
        int tMin,        String domain,        int tMax        ArrayList<myffbd_Function> myffbd_functions    ) {
        this.tMin = tMin;
        this.domain = domain;
        this.tMax = tMax;
        this.myffbd_functions = myffbd_functions;
    }

    public int getTmin() {
        return tMin;
    }

    public void setTmin(int tMin) {
        this.tMin = tMin;
    }
    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }
    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
    }

    public List<myffbd_Function> getMyffbd_functions() {
        return myffbd_functions;
    }

    public void addMyffbd_function(Myffbd_function myffbd_function) {
        this.myffbd_functions.add(myffbd_function);
    }

}