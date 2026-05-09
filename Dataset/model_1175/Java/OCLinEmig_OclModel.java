





import java.util.List;
import java.util.ArrayList;

public class OCLinEmig_OclModel extends LocatedElement {

    private String name;





    private List<OCLinEmig_OclModel> oclinemig_oclmodels;




    private OCLinEmig_OclModel oclinemig_oclmodel;


    public OCLinEmig_OclModel(
        String name    ) {
        super(
        );
        this.name = name;
        this.oclinemig_oclmodels = new ArrayList<>();
    }

    public OCLinEmig_OclModel(
        String name        ArrayList<OCLinEmig_OclModel> oclinemig_oclmodels    ) {
        this.name = name;
        this.oclinemig_oclmodels = oclinemig_oclmodels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<OCLinEmig_OclModel> getOclinemig_oclmodels() {
        return oclinemig_oclmodels;
    }

    public void addOclinemig_oclmodel(Oclinemig_oclmodel oclinemig_oclmodel) {
        this.oclinemig_oclmodels.add(oclinemig_oclmodel);
    }
    public OCLinEmig_OclModel getOclinemig_oclmodel() {
        return oclinemig_oclmodel;
    }

    public void setOclinemig_oclmodel(OCLinEmig_OclModel oclinemig_oclmodel) {
        this.oclinemig_oclmodel = oclinemig_oclmodel;
    }

}