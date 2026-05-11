





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpre__Waitress extends MTpre__Element {

    private String MTpre__name;





    private List<ramRoot_MTpre__Table> ramroot_mtpre__tables;




    private ramRoot_MTpre__Restaurant ramroot_mtpre__restaurant;


    public ramRoot_MTpre__Waitress(
        String MTpre__name    ) {
        super(
        );
        this.MTpre__name = MTpre__name;
        this.ramroot_mtpre__tables = new ArrayList<>();
    }

    public ramRoot_MTpre__Waitress(
        String MTpre__name        ArrayList<ramRoot_MTpre__Table> ramroot_mtpre__tables    ) {
        this.MTpre__name = MTpre__name;
        this.ramroot_mtpre__tables = ramroot_mtpre__tables;
    }

    public String getMtpre__name() {
        return MTpre__name;
    }

    public void setMtpre__name(String MTpre__name) {
        this.MTpre__name = MTpre__name;
    }

    public List<ramRoot_MTpre__Table> getRamroot_mtpre__tables() {
        return ramroot_mtpre__tables;
    }

    public void addRamroot_mtpre__table(Ramroot_mtpre__table ramroot_mtpre__table) {
        this.ramroot_mtpre__tables.add(ramroot_mtpre__table);
    }
    public ramRoot_MTpre__Restaurant getRamroot_mtpre__restaurant() {
        return ramroot_mtpre__restaurant;
    }

    public void setRamroot_mtpre__restaurant(ramRoot_MTpre__Restaurant ramroot_mtpre__restaurant) {
        this.ramroot_mtpre__restaurant = ramroot_mtpre__restaurant;
    }

}