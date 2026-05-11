





import java.util.List;
import java.util.ArrayList;

public class formalmetamodel_B  {

    private String name;





    private List<formalmetamodel_A> formalmetamodel_as;




    private formalmetamodel_A formalmetamodel_a;




    private formalmetamodel_B formalmetamodel_b;


    public formalmetamodel_B(
        String name    ) {
        this.name = name;
        this.formalmetamodel_as = new ArrayList<>();
    }

    public formalmetamodel_B(
        String name        ArrayList<formalmetamodel_A> formalmetamodel_as    ) {
        this.name = name;
        this.formalmetamodel_as = formalmetamodel_as;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<formalmetamodel_A> getFormalmetamodel_as() {
        return formalmetamodel_as;
    }

    public void addFormalmetamodel_a(Formalmetamodel_a formalmetamodel_a) {
        this.formalmetamodel_as.add(formalmetamodel_a);
    }
    public formalmetamodel_A getFormalmetamodel_a() {
        return formalmetamodel_a;
    }

    public void setFormalmetamodel_a(formalmetamodel_A formalmetamodel_a) {
        this.formalmetamodel_a = formalmetamodel_a;
    }
    public formalmetamodel_B getFormalmetamodel_b() {
        return formalmetamodel_b;
    }

    public void setFormalmetamodel_b(formalmetamodel_B formalmetamodel_b) {
        this.formalmetamodel_b = formalmetamodel_b;
    }

}