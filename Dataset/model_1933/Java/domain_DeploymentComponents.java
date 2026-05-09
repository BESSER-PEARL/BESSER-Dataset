





import java.util.List;
import java.util.ArrayList;

public class domain_DeploymentComponents  {

    private String uid;





    private domain_EObject domain_eobject;




    private domain_DeploymentSequence domain_deploymentsequence;


    public domain_DeploymentComponents(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }
    public domain_DeploymentSequence getDomain_deploymentsequence() {
        return domain_deploymentsequence;
    }

    public void setDomain_deploymentsequence(domain_DeploymentSequence domain_deploymentsequence) {
        this.domain_deploymentsequence = domain_deploymentsequence;
    }

}