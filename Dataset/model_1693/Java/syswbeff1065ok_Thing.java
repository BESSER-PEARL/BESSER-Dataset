





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_Thing  {

    private int id;





    private syswbeff1065ok_AssociatedTo syswbeff1065ok_associatedto;




    private syswbeff1065ok_AssociatedTo syswbeff1065ok_associatedto;




    private List<syswbeff1065ok_AssociatedTo> syswbeff1065ok_associatedtos;


    public syswbeff1065ok_Thing(
        int id    ) {
        this.id = id;
        this.syswbeff1065ok_associatedtos = new ArrayList<>();
    }

    public syswbeff1065ok_Thing(
        int id        ArrayList<syswbeff1065ok_AssociatedTo> syswbeff1065ok_associatedtos    ) {
        this.id = id;
        this.syswbeff1065ok_associatedtos = syswbeff1065ok_associatedtos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public syswbeff1065ok_AssociatedTo getSyswbeff1065ok_associatedto() {
        return syswbeff1065ok_associatedto;
    }

    public void setSyswbeff1065ok_associatedto(syswbeff1065ok_AssociatedTo syswbeff1065ok_associatedto) {
        this.syswbeff1065ok_associatedto = syswbeff1065ok_associatedto;
    }
    public syswbeff1065ok_AssociatedTo getSyswbeff1065ok_associatedto() {
        return syswbeff1065ok_associatedto;
    }

    public void setSyswbeff1065ok_associatedto(syswbeff1065ok_AssociatedTo syswbeff1065ok_associatedto) {
        this.syswbeff1065ok_associatedto = syswbeff1065ok_associatedto;
    }
    public List<syswbeff1065ok_AssociatedTo> getSyswbeff1065ok_associatedtos() {
        return syswbeff1065ok_associatedtos;
    }

    public void addSyswbeff1065ok_associatedto(Syswbeff1065ok_associatedto syswbeff1065ok_associatedto) {
        this.syswbeff1065ok_associatedtos.add(syswbeff1065ok_associatedto);
    }

}