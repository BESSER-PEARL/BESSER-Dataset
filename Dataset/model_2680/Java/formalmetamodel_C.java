





import java.util.List;
import java.util.ArrayList;

public class formalmetamodel_C  {

    private String name;





    private List<formalmetamodel_C> formalmetamodel_cs;




    private formalmetamodel_A formalmetamodel_a;




    private formalmetamodel_FormalModel formalmetamodel_formalmodel;


    public formalmetamodel_C(
        String name    ) {
        this.name = name;
        this.formalmetamodel_cs = new ArrayList<>();
    }

    public formalmetamodel_C(
        String name        ArrayList<formalmetamodel_C> formalmetamodel_cs    ) {
        this.name = name;
        this.formalmetamodel_cs = formalmetamodel_cs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<formalmetamodel_C> getFormalmetamodel_cs() {
        return formalmetamodel_cs;
    }

    public void addFormalmetamodel_c(Formalmetamodel_c formalmetamodel_c) {
        this.formalmetamodel_cs.add(formalmetamodel_c);
    }
    public formalmetamodel_A getFormalmetamodel_a() {
        return formalmetamodel_a;
    }

    public void setFormalmetamodel_a(formalmetamodel_A formalmetamodel_a) {
        this.formalmetamodel_a = formalmetamodel_a;
    }
    public formalmetamodel_FormalModel getFormalmetamodel_formalmodel() {
        return formalmetamodel_formalmodel;
    }

    public void setFormalmetamodel_formalmodel(formalmetamodel_FormalModel formalmetamodel_formalmodel) {
        this.formalmetamodel_formalmodel = formalmetamodel_formalmodel;
    }

}