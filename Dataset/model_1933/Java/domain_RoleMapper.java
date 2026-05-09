





import java.util.List;
import java.util.ArrayList;

public class domain_RoleMapper extends Mapper {

    private String globalRoleName;
    private String fakeRoleName;
    private String localRoleName;





    private domain_EObject domain_eobject;


    public domain_RoleMapper(
        String globalRoleName,        String fakeRoleName,        String localRoleName    ) {
        super(
        );
        this.globalRoleName = globalRoleName;
        this.fakeRoleName = fakeRoleName;
        this.localRoleName = localRoleName;
    }


    public String getGlobalrolename() {
        return globalRoleName;
    }

    public void setGlobalrolename(String globalRoleName) {
        this.globalRoleName = globalRoleName;
    }
    public String getFakerolename() {
        return fakeRoleName;
    }

    public void setFakerolename(String fakeRoleName) {
        this.fakeRoleName = fakeRoleName;
    }
    public String getLocalrolename() {
        return localRoleName;
    }

    public void setLocalrolename(String localRoleName) {
        this.localRoleName = localRoleName;
    }

    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }

}