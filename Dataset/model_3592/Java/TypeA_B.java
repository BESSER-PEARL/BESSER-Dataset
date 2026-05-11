





import java.util.List;
import java.util.ArrayList;

public class TypeA_B  {

    private String nameB;





    private TypeA_A typea_a;




    private List<TypeA_A> typea_as;


    public TypeA_B(
        String nameB    ) {
        this.nameB = nameB;
        this.typea_as = new ArrayList<>();
    }

    public TypeA_B(
        String nameB        ArrayList<TypeA_A> typea_as    ) {
        this.nameB = nameB;
        this.typea_as = typea_as;
    }

    public String getNameb() {
        return nameB;
    }

    public void setNameb(String nameB) {
        this.nameB = nameB;
    }

    public TypeA_A getTypea_a() {
        return typea_a;
    }

    public void setTypea_a(TypeA_A typea_a) {
        this.typea_a = typea_a;
    }
    public List<TypeA_A> getTypea_as() {
        return typea_as;
    }

    public void addTypea_a(Typea_a typea_a) {
        this.typea_as.add(typea_a);
    }

}