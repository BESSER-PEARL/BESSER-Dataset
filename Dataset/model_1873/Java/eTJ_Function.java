





import java.util.List;
import java.util.ArrayList;

public class eTJ_Function  {

    private int level;
    private String parentId;
    private int distance;





    private eTJ_ISODATE etj_isodate;




    private eTJ_LogicalFunctionExpression etj_logicalfunctionexpression;




    private eTJ_Scenario etj_scenario;




    private eTJ_Task etj_task;




    private eTJ_Resource etj_resource;


    public eTJ_Function(
        int level,        String parentId,        int distance    ) {
        this.level = level;
        this.parentId = parentId;
        this.distance = distance;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getParentid() {
        return parentId;
    }

    public void setParentid(String parentId) {
        this.parentId = parentId;
    }
    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

    public eTJ_ISODATE getEtj_isodate() {
        return etj_isodate;
    }

    public void setEtj_isodate(eTJ_ISODATE etj_isodate) {
        this.etj_isodate = etj_isodate;
    }
    public eTJ_LogicalFunctionExpression getEtj_logicalfunctionexpression() {
        return etj_logicalfunctionexpression;
    }

    public void setEtj_logicalfunctionexpression(eTJ_LogicalFunctionExpression etj_logicalfunctionexpression) {
        this.etj_logicalfunctionexpression = etj_logicalfunctionexpression;
    }
    public eTJ_Scenario getEtj_scenario() {
        return etj_scenario;
    }

    public void setEtj_scenario(eTJ_Scenario etj_scenario) {
        this.etj_scenario = etj_scenario;
    }
    public eTJ_Task getEtj_task() {
        return etj_task;
    }

    public void setEtj_task(eTJ_Task etj_task) {
        this.etj_task = etj_task;
    }
    public eTJ_Resource getEtj_resource() {
        return etj_resource;
    }

    public void setEtj_resource(eTJ_Resource etj_resource) {
        this.etj_resource = etj_resource;
    }

}