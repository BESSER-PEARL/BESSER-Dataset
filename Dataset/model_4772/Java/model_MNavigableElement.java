





import java.util.List;
import java.util.ArrayList;

public class model_MNavigableElement  {

    private String nameAsRolename;





    private model_MClass model_mclass;




    private model_MAssociation model_massociation;


    public model_MNavigableElement(
        String nameAsRolename    ) {
        this.nameAsRolename = nameAsRolename;
    }


    public String getNameasrolename() {
        return nameAsRolename;
    }

    public void setNameasrolename(String nameAsRolename) {
        this.nameAsRolename = nameAsRolename;
    }

    public model_MClass getModel_mclass() {
        return model_mclass;
    }

    public void setModel_mclass(model_MClass model_mclass) {
        this.model_mclass = model_mclass;
    }
    public model_MAssociation getModel_massociation() {
        return model_massociation;
    }

    public void setModel_massociation(model_MAssociation model_massociation) {
        this.model_massociation = model_massociation;
    }

}