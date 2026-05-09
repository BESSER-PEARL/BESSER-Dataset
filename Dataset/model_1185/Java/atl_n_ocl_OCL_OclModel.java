





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_OCL_OclModel  {

    private String name;





    private OclModel oclmodel;




    private List<OclModel> oclmodels;


    public atl_n_ocl_OCL_OclModel(
        String name    ) {
        this.name = name;
        this.oclmodels = new ArrayList<>();
    }

    public atl_n_ocl_OCL_OclModel(
        String name        ArrayList<OclModel> oclmodels    ) {
        this.name = name;
        this.oclmodels = oclmodels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public OclModel getOclmodel() {
        return oclmodel;
    }

    public void setOclmodel(OclModel oclmodel) {
        this.oclmodel = oclmodel;
    }
    public List<OclModel> getOclmodels() {
        return oclmodels;
    }

    public void addOclmodel(Oclmodel oclmodel) {
        this.oclmodels.add(oclmodel);
    }

}