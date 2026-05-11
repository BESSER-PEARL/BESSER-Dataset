





import java.util.List;
import java.util.ArrayList;

public class ref_unsettable_C2U  {






    private List<BU> bus;




    private AU au;


    public ref_unsettable_C2U(
    ) {
        this.bus = new ArrayList<>();
    }

    public ref_unsettable_C2U(
        ArrayList<BU> bus    ) {
        this.bus = bus;
    }


    public List<BU> getBus() {
        return bus;
    }

    public void addBu(Bu bu) {
        this.bus.add(bu);
    }
    public AU getAu() {
        return au;
    }

    public void setAu(AU au) {
        this.au = au;
    }

}