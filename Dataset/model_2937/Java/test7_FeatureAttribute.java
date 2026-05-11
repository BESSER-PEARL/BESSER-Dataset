





import java.util.List;
import java.util.ArrayList;

public class test7_FeatureAttribute  {

    private String name;





    private test7_AttributeType test7_attributetype;




    private test7_Model test7_model;




    private test7_FiniteDomainSC test7_finitedomainsc;


    public test7_FeatureAttribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public test7_AttributeType getTest7_attributetype() {
        return test7_attributetype;
    }

    public void setTest7_attributetype(test7_AttributeType test7_attributetype) {
        this.test7_attributetype = test7_attributetype;
    }
    public test7_Model getTest7_model() {
        return test7_model;
    }

    public void setTest7_model(test7_Model test7_model) {
        this.test7_model = test7_model;
    }
    public test7_FiniteDomainSC getTest7_finitedomainsc() {
        return test7_finitedomainsc;
    }

    public void setTest7_finitedomainsc(test7_FiniteDomainSC test7_finitedomainsc) {
        this.test7_finitedomainsc = test7_finitedomainsc;
    }

}