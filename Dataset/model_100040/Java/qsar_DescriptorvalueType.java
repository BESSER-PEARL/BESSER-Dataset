





import java.util.List;
import java.util.ArrayList;

public class qsar_DescriptorvalueType  {

    private String index;
    private String value;
    private String label;





    private qsar_DescriptorresultType qsar_descriptorresulttype;


    public qsar_DescriptorvalueType(
        String index,        String value,        String label    ) {
        this.index = index;
        this.value = value;
        this.label = label;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public qsar_DescriptorresultType getQsar_descriptorresulttype() {
        return qsar_descriptorresulttype;
    }

    public void setQsar_descriptorresulttype(qsar_DescriptorresultType qsar_descriptorresulttype) {
        this.qsar_descriptorresulttype = qsar_descriptorresulttype;
    }

}