





import java.util.List;
import java.util.ArrayList;

public class gore_DifferentialRelation  {

    private String upperBound;
    private String operator;
    private String lowerBound;
    private float value;





    private gore_Parameter gore_parameter;




    private gore_GoalModel gore_goalmodel;




    private gore_AwReq gore_awreq;


    public gore_DifferentialRelation(
        String upperBound,        String operator,        String lowerBound,        float value    ) {
        this.upperBound = upperBound;
        this.operator = operator;
        this.lowerBound = lowerBound;
        this.value = value;
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
    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public gore_Parameter getGore_parameter() {
        return gore_parameter;
    }

    public void setGore_parameter(gore_Parameter gore_parameter) {
        this.gore_parameter = gore_parameter;
    }
    public gore_GoalModel getGore_goalmodel() {
        return gore_goalmodel;
    }

    public void setGore_goalmodel(gore_GoalModel gore_goalmodel) {
        this.gore_goalmodel = gore_goalmodel;
    }
    public gore_AwReq getGore_awreq() {
        return gore_awreq;
    }

    public void setGore_awreq(gore_AwReq gore_awreq) {
        this.gore_awreq = gore_awreq;
    }

}