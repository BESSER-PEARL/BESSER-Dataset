





import java.util.List;
import java.util.ArrayList;

public class domain_MappingSpecifier  {

    private String uid;





    private domain_Specifier domain_specifier;




    private domain_ModelMapper domain_modelmapper;




    private domain_Option domain_option;


    public domain_MappingSpecifier(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Specifier getDomain_specifier() {
        return domain_specifier;
    }

    public void setDomain_specifier(domain_Specifier domain_specifier) {
        this.domain_specifier = domain_specifier;
    }
    public domain_ModelMapper getDomain_modelmapper() {
        return domain_modelmapper;
    }

    public void setDomain_modelmapper(domain_ModelMapper domain_modelmapper) {
        this.domain_modelmapper = domain_modelmapper;
    }
    public domain_Option getDomain_option() {
        return domain_option;
    }

    public void setDomain_option(domain_Option domain_option) {
        this.domain_option = domain_option;
    }

}