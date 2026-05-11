





import java.util.List;
import java.util.ArrayList;

public class TypeB_A  {

    private String name;





    private TypeB_B typeb_b;




    private List<TypeB_B> typeb_bs;


    public TypeB_A(
        String name    ) {
        this.name = name;
        this.typeb_bs = new ArrayList<>();
    }

    public TypeB_A(
        String name        ArrayList<TypeB_B> typeb_bs    ) {
        this.name = name;
        this.typeb_bs = typeb_bs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public TypeB_B getTypeb_b() {
        return typeb_b;
    }

    public void setTypeb_b(TypeB_B typeb_b) {
        this.typeb_b = typeb_b;
    }
    public List<TypeB_B> getTypeb_bs() {
        return typeb_bs;
    }

    public void addTypeb_b(Typeb_b typeb_b) {
        this.typeb_bs.add(typeb_b);
    }

}