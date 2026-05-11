





import java.util.List;
import java.util.ArrayList;

public class fragdial_Interface  {

    private String startProperty;
    private String signature;
    private String contingency;
    private String name;
    private String cardinality;



    public fragdial_Interface(
        String startProperty,        String signature,        String contingency,        String name,        String cardinality    ) {
        this.startProperty = startProperty;
        this.signature = signature;
        this.contingency = contingency;
        this.name = name;
        this.cardinality = cardinality;
    }


    public String getStartproperty() {
        return startProperty;
    }

    public void setStartproperty(String startProperty) {
        this.startProperty = startProperty;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getContingency() {
        return contingency;
    }

    public void setContingency(String contingency) {
        this.contingency = contingency;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }


}