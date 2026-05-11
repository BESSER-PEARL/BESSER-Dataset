





import java.util.List;
import java.util.ArrayList;

public class formalmetamodel_FormalModel  {






    private List<formalmetamodel_B> formalmetamodel_bs;




    private List<formalmetamodel_A> formalmetamodel_as;


    public formalmetamodel_FormalModel(
    ) {
        this.formalmetamodel_bs = new ArrayList<>();
        this.formalmetamodel_as = new ArrayList<>();
    }

    public formalmetamodel_FormalModel(
        ArrayList<formalmetamodel_B> formalmetamodel_bs,        ArrayList<formalmetamodel_A> formalmetamodel_as    ) {
        this.formalmetamodel_bs = formalmetamodel_bs;
        this.formalmetamodel_as = formalmetamodel_as;
    }


    public List<formalmetamodel_B> getFormalmetamodel_bs() {
        return formalmetamodel_bs;
    }

    public void addFormalmetamodel_b(Formalmetamodel_b formalmetamodel_b) {
        this.formalmetamodel_bs.add(formalmetamodel_b);
    }
    public List<formalmetamodel_A> getFormalmetamodel_as() {
        return formalmetamodel_as;
    }

    public void addFormalmetamodel_a(Formalmetamodel_a formalmetamodel_a) {
        this.formalmetamodel_as.add(formalmetamodel_a);
    }

}