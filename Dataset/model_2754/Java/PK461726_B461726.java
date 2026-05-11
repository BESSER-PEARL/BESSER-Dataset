





import java.util.List;
import java.util.ArrayList;

public class PK461726_B461726  {

    private String name;





    private PK461726_A461726 pk461726_a461726;




    private List<PK461726_A461726> pk461726_a461726s;


    public PK461726_B461726(
        String name    ) {
        this.name = name;
        this.pk461726_a461726s = new ArrayList<>();
    }

    public PK461726_B461726(
        String name        ArrayList<PK461726_A461726> pk461726_a461726s    ) {
        this.name = name;
        this.pk461726_a461726s = pk461726_a461726s;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PK461726_A461726 getPk461726_a461726() {
        return pk461726_a461726;
    }

    public void setPk461726_a461726(PK461726_A461726 pk461726_a461726) {
        this.pk461726_a461726 = pk461726_a461726;
    }
    public List<PK461726_A461726> getPk461726_a461726s() {
        return pk461726_a461726s;
    }

    public void addPk461726_a461726(Pk461726_a461726 pk461726_a461726) {
        this.pk461726_a461726s.add(pk461726_a461726);
    }

}