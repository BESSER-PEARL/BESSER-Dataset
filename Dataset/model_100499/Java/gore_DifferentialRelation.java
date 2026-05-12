





import java.util.List;
import java.util.ArrayList;

public class gore_DifferentialRelation  {

    private float value;
    private String lowerBound;
    private String upperBound;
    private String operator;





    private gore_Parameter gore_parameter;




    private gore_AwReq gore_awreq;


    public gore_DifferentialRelation(
        float value,        String lowerBound,        String upperBound,        String operator    ) {
        this.value = value;
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        this.operator = operator;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public gore_Parameter getGore_parameter() {
        return gore_parameter;
    }

    public void setGore_parameter(gore_Parameter gore_parameter) {
        this.gore_parameter = gore_parameter;
    }
    public gore_AwReq getGore_awreq() {
        return gore_awreq;
    }

    public void setGore_awreq(gore_AwReq gore_awreq) {
        this.gore_awreq = gore_awreq;
    }

}