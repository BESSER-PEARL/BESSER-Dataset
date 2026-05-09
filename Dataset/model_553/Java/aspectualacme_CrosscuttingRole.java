





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_CrosscuttingRole extends Role {






    private aspectualacme_Glue aspectualacme_glue;




    private List<aspectualacme_RoleType> aspectualacme_roletypes;


    public aspectualacme_CrosscuttingRole(
    ) {
        super(
        );
        this.aspectualacme_roletypes = new ArrayList<>();
    }

    public aspectualacme_CrosscuttingRole(
        ArrayList<aspectualacme_RoleType> aspectualacme_roletypes    ) {
        this.aspectualacme_roletypes = aspectualacme_roletypes;
    }


    public aspectualacme_Glue getAspectualacme_glue() {
        return aspectualacme_glue;
    }

    public void setAspectualacme_glue(aspectualacme_Glue aspectualacme_glue) {
        this.aspectualacme_glue = aspectualacme_glue;
    }
    public List<aspectualacme_RoleType> getAspectualacme_roletypes() {
        return aspectualacme_roletypes;
    }

    public void addAspectualacme_roletype(Aspectualacme_roletype aspectualacme_roletype) {
        this.aspectualacme_roletypes.add(aspectualacme_roletype);
    }

}