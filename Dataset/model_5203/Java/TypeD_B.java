





import java.util.List;
import java.util.ArrayList;

public class TypeD_B  {

    private String name;





    private List<TypeD_A> typed_as;




    private TypeD_A typed_a;


    public TypeD_B(
        String name    ) {
        this.name = name;
        this.typed_as = new ArrayList<>();
    }

    public TypeD_B(
        String name        ArrayList<TypeD_A> typed_as    ) {
        this.name = name;
        this.typed_as = typed_as;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<TypeD_A> getTyped_as() {
        return typed_as;
    }

    public void addTyped_a(Typed_a typed_a) {
        this.typed_as.add(typed_a);
    }
    public TypeD_A getTyped_a() {
        return typed_a;
    }

    public void setTyped_a(TypeD_A typed_a) {
        this.typed_a = typed_a;
    }

}