





import java.util.List;
import java.util.ArrayList;

public class qsar_ParameterType  {

    private String key;
    private String value;





    private qsar_DescriptorType qsar_descriptortype;


    public qsar_ParameterType(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public qsar_DescriptorType getQsar_descriptortype() {
        return qsar_descriptortype;
    }

    public void setQsar_descriptortype(qsar_DescriptorType qsar_descriptortype) {
        this.qsar_descriptortype = qsar_descriptortype;
    }

}