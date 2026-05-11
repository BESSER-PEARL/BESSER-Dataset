





import java.util.List;
import java.util.ArrayList;

public class emfdb_D  {

    private String name;





    private emfdb_B emfdb_b;


    public emfdb_D(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emfdb_B getEmfdb_b() {
        return emfdb_b;
    }

    public void setEmfdb_b(emfdb_B emfdb_b) {
        this.emfdb_b = emfdb_b;
    }

}