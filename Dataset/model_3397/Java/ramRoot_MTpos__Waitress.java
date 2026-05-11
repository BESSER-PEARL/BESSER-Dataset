





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpos__Waitress extends MTpos__Element {

    private String MTpos__name;





    private List<ramRoot_MTpos__Table> ramroot_mtpos__tables;


    public ramRoot_MTpos__Waitress(
        String MTpos__name    ) {
        super(
        );
        this.MTpos__name = MTpos__name;
        this.ramroot_mtpos__tables = new ArrayList<>();
    }

    public ramRoot_MTpos__Waitress(
        String MTpos__name        ArrayList<ramRoot_MTpos__Table> ramroot_mtpos__tables    ) {
        this.MTpos__name = MTpos__name;
        this.ramroot_mtpos__tables = ramroot_mtpos__tables;
    }

    public String getMtpos__name() {
        return MTpos__name;
    }

    public void setMtpos__name(String MTpos__name) {
        this.MTpos__name = MTpos__name;
    }

    public List<ramRoot_MTpos__Table> getRamroot_mtpos__tables() {
        return ramroot_mtpos__tables;
    }

    public void addRamroot_mtpos__table(Ramroot_mtpos__table ramroot_mtpos__table) {
        this.ramroot_mtpos__tables.add(ramroot_mtpos__table);
    }

}