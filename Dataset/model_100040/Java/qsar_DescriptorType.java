





import java.util.List;
import java.util.ArrayList;

public class qsar_DescriptorType  {

    private String provider;
    private String id;
    private String ontologyid;





    private qsar_DescriptorlistType qsar_descriptorlisttype;


    public qsar_DescriptorType(
        String provider,        String id,        String ontologyid    ) {
        this.provider = provider;
        this.id = id;
        this.ontologyid = ontologyid;
    }


    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getOntologyid() {
        return ontologyid;
    }

    public void setOntologyid(String ontologyid) {
        this.ontologyid = ontologyid;
    }

    public qsar_DescriptorlistType getQsar_descriptorlisttype() {
        return qsar_descriptorlisttype;
    }

    public void setQsar_descriptorlisttype(qsar_DescriptorlistType qsar_descriptorlisttype) {
        this.qsar_descriptorlisttype = qsar_descriptorlisttype;
    }

}