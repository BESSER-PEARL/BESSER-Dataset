





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_BaseRole extends Role {






    private aspectualacme_Glue aspectualacme_glue;




    private List<aspectualacme_RoleType> aspectualacme_roletypes;


    public aspectualacme_BaseRole(
    ) {
        super(
        );
        this.aspectualacme_roletypes = new ArrayList<>();
    }

    public aspectualacme_BaseRole(
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