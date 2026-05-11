





import java.util.List;
import java.util.ArrayList;

public class emfdb_A  {

    private String string;





    private List<emfdb_C> emfdb_cs;


    public emfdb_A(
        String string    ) {
        this.string = string;
        this.emfdb_cs = new ArrayList<>();
    }

    public emfdb_A(
        String string        ArrayList<emfdb_C> emfdb_cs    ) {
        this.string = string;
        this.emfdb_cs = emfdb_cs;
    }

    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public List<emfdb_C> getEmfdb_cs() {
        return emfdb_cs;
    }

    public void addEmfdb_c(Emfdb_c emfdb_c) {
        this.emfdb_cs.add(emfdb_c);
    }

}