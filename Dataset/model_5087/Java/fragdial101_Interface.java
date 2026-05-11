





import java.util.List;
import java.util.ArrayList;

public class fragdial101_Interface  {

    private String contingency;
    private String signature;
    private String cardinality;
    private String startProperty;
    private String name;



    public fragdial101_Interface(
        String contingency,        String signature,        String cardinality,        String startProperty,        String name    ) {
        this.contingency = contingency;
        this.signature = signature;
        this.cardinality = cardinality;
        this.startProperty = startProperty;
        this.name = name;
    }


    public String getContingency() {
        return contingency;
    }

    public void setContingency(String contingency) {
        this.contingency = contingency;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getStartproperty() {
        return startProperty;
    }

    public void setStartproperty(String startProperty) {
        this.startProperty = startProperty;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}