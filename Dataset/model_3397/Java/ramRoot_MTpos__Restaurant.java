





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpos__Restaurant extends MTpos__Element {






    private List<ramRoot_MTpos__Waitress> ramroot_mtpos__waitresss;




    private List<ramRoot_MTpos__Table> ramroot_mtpos__tables;


    public ramRoot_MTpos__Restaurant(
    ) {
        super(
        );
        this.ramroot_mtpos__waitresss = new ArrayList<>();
        this.ramroot_mtpos__tables = new ArrayList<>();
    }

    public ramRoot_MTpos__Restaurant(
        ArrayList<ramRoot_MTpos__Waitress> ramroot_mtpos__waitresss,        ArrayList<ramRoot_MTpos__Table> ramroot_mtpos__tables    ) {
        this.ramroot_mtpos__waitresss = ramroot_mtpos__waitresss;
        this.ramroot_mtpos__tables = ramroot_mtpos__tables;
    }


    public List<ramRoot_MTpos__Waitress> getRamroot_mtpos__waitresss() {
        return ramroot_mtpos__waitresss;
    }

    public void addRamroot_mtpos__waitress(Ramroot_mtpos__waitress ramroot_mtpos__waitress) {
        this.ramroot_mtpos__waitresss.add(ramroot_mtpos__waitress);
    }
    public List<ramRoot_MTpos__Table> getRamroot_mtpos__tables() {
        return ramroot_mtpos__tables;
    }

    public void addRamroot_mtpos__table(Ramroot_mtpos__table ramroot_mtpos__table) {
        this.ramroot_mtpos__tables.add(ramroot_mtpos__table);
    }

}