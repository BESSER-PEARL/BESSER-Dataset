





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpre__Restaurant extends MTpre__Element {






    private List<ramRoot_MTpre__Table> ramroot_mtpre__tables;


    public ramRoot_MTpre__Restaurant(
    ) {
        super(
        );
        this.ramroot_mtpre__tables = new ArrayList<>();
    }

    public ramRoot_MTpre__Restaurant(
        ArrayList<ramRoot_MTpre__Table> ramroot_mtpre__tables    ) {
        this.ramroot_mtpre__tables = ramroot_mtpre__tables;
    }


    public List<ramRoot_MTpre__Table> getRamroot_mtpre__tables() {
        return ramroot_mtpre__tables;
    }

    public void addRamroot_mtpre__table(Ramroot_mtpre__table ramroot_mtpre__table) {
        this.ramroot_mtpre__tables.add(ramroot_mtpre__table);
    }

}