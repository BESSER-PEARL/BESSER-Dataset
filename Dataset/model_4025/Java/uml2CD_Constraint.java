





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Constraint  {

    private String specification;





    private uml2CD_NamedElement uml2cd_namedelement;


    public uml2CD_Constraint(
        String specification    ) {
        this.specification = specification;
    }


    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }

    public uml2CD_NamedElement getUml2cd_namedelement() {
        return uml2cd_namedelement;
    }

    public void setUml2cd_namedelement(uml2CD_NamedElement uml2cd_namedelement) {
        this.uml2cd_namedelement = uml2cd_namedelement;
    }

}