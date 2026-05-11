





import java.util.List;
import java.util.ArrayList;

public class vM_Email  {

    private String username;
    private String domain;





    private vM_MetaDataDeclaration vm_metadatadeclaration;


    public vM_Email(
        String username,        String domain    ) {
        this.username = username;
        this.domain = domain;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public vM_MetaDataDeclaration getVm_metadatadeclaration() {
        return vm_metadatadeclaration;
    }

    public void setVm_metadatadeclaration(vM_MetaDataDeclaration vm_metadatadeclaration) {
        this.vm_metadatadeclaration = vm_metadatadeclaration;
    }

}