





import java.util.List;
import java.util.ArrayList;

public class TypeB_B  {

    private String name;





    private TypeB_A typeb_a;




    private TypeB_A typeb_a;




    private TypeB_A typeb_a;




    private List<TypeB_A> typeb_as;


    public TypeB_B(
        String name    ) {
        this.name = name;
        this.typeb_as = new ArrayList<>();
    }

    public TypeB_B(
        String name        ArrayList<TypeB_A> typeb_as    ) {
        this.name = name;
        this.typeb_as = typeb_as;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public TypeB_A getTypeb_a() {
        return typeb_a;
    }

    public void setTypeb_a(TypeB_A typeb_a) {
        this.typeb_a = typeb_a;
    }
    public TypeB_A getTypeb_a() {
        return typeb_a;
    }

    public void setTypeb_a(TypeB_A typeb_a) {
        this.typeb_a = typeb_a;
    }
    public TypeB_A getTypeb_a() {
        return typeb_a;
    }

    public void setTypeb_a(TypeB_A typeb_a) {
        this.typeb_a = typeb_a;
    }
    public List<TypeB_A> getTypeb_as() {
        return typeb_as;
    }

    public void addTypeb_a(Typeb_a typeb_a) {
        this.typeb_as.add(typeb_a);
    }

}