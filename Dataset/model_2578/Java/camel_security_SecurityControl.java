





import java.util.List;
import java.util.ArrayList;

public class camel_security_SecurityControl  {

    private String name;
    private String specification;





    private List<RawSecurityMetric> rawsecuritymetrics;




    private SecurityDomain securitydomain;




    private SecurityDomain securitydomain;




    private List<SecurityProperty> securitypropertys;




    private List<CompositeSecurityMetric> compositesecuritymetrics;


    public camel_security_SecurityControl(
        String name,        String specification    ) {
        this.name = name;
        this.specification = specification;
        this.rawsecuritymetrics = new ArrayList<>();
        this.securitypropertys = new ArrayList<>();
        this.compositesecuritymetrics = new ArrayList<>();
    }

    public camel_security_SecurityControl(
        String name,        String specification        ArrayList<RawSecurityMetric> rawsecuritymetrics,        ArrayList<SecurityProperty> securitypropertys,        ArrayList<CompositeSecurityMetric> compositesecuritymetrics    ) {
        this.name = name;
        this.specification = specification;
        this.rawsecuritymetrics = rawsecuritymetrics;
        this.securitypropertys = securitypropertys;
        this.compositesecuritymetrics = compositesecuritymetrics;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }

    public List<RawSecurityMetric> getRawsecuritymetrics() {
        return rawsecuritymetrics;
    }

    public void addRawsecuritymetric(Rawsecuritymetric rawsecuritymetric) {
        this.rawsecuritymetrics.add(rawsecuritymetric);
    }
    public SecurityDomain getSecuritydomain() {
        return securitydomain;
    }

    public void setSecuritydomain(SecurityDomain securitydomain) {
        this.securitydomain = securitydomain;
    }
    public SecurityDomain getSecuritydomain() {
        return securitydomain;
    }

    public void setSecuritydomain(SecurityDomain securitydomain) {
        this.securitydomain = securitydomain;
    }
    public List<SecurityProperty> getSecuritypropertys() {
        return securitypropertys;
    }

    public void addSecurityproperty(Securityproperty securityproperty) {
        this.securitypropertys.add(securityproperty);
    }
    public List<CompositeSecurityMetric> getCompositesecuritymetrics() {
        return compositesecuritymetrics;
    }

    public void addCompositesecuritymetric(Compositesecuritymetric compositesecuritymetric) {
        this.compositesecuritymetrics.add(compositesecuritymetric);
    }

}