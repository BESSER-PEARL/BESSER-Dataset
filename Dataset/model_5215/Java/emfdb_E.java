





import java.util.List;
import java.util.ArrayList;

public class emfdb_E  {

    private String name;





    private emfdb_D emfdb_d;


    public emfdb_E(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emfdb_D getEmfdb_d() {
        return emfdb_d;
    }

    public void setEmfdb_d(emfdb_D emfdb_d) {
        this.emfdb_d = emfdb_d;
    }

}