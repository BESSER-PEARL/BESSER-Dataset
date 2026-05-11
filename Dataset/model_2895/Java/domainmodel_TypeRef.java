





import java.util.List;
import java.util.ArrayList;

public class domainmodel_TypeRef  {

    private boolean multi;





    private domainmodel_TypedElement domainmodel_typedelement;




    private domainmodel_Type domainmodel_type;


    public domainmodel_TypeRef(
        boolean multi    ) {
        this.multi = multi;
    }


    public boolean getMulti() {
        return multi;
    }

    public void setMulti(boolean multi) {
        this.multi = multi;
    }

    public domainmodel_TypedElement getDomainmodel_typedelement() {
        return domainmodel_typedelement;
    }

    public void setDomainmodel_typedelement(domainmodel_TypedElement domainmodel_typedelement) {
        this.domainmodel_typedelement = domainmodel_typedelement;
    }
    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }

}