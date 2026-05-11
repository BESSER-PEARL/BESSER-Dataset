





import java.util.List;
import java.util.ArrayList;

public class TypeA_A  {

    private String name;





    private List<TypeA_C> typea_cs;


    public TypeA_A(
        String name    ) {
        this.name = name;
        this.typea_cs = new ArrayList<>();
    }

    public TypeA_A(
        String name        ArrayList<TypeA_C> typea_cs    ) {
        this.name = name;
        this.typea_cs = typea_cs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<TypeA_C> getTypea_cs() {
        return typea_cs;
    }

    public void addTypea_c(Typea_c typea_c) {
        this.typea_cs.add(typea_c);
    }

}