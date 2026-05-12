





import java.util.List;
import java.util.ArrayList;

public class releng_Promotion  {

    private String buildType;





    private List<releng_Criterion> releng_criterions;




    private releng_BuildJob releng_buildjob;




    private releng_Repository releng_repository;




    private releng_BuildJob releng_buildjob;


    public releng_Promotion(
        String buildType    ) {
        this.buildType = buildType;
        this.releng_criterions = new ArrayList<>();
    }

    public releng_Promotion(
        String buildType        ArrayList<releng_Criterion> releng_criterions    ) {
        this.buildType = buildType;
        this.releng_criterions = releng_criterions;
    }

    public String getBuildtype() {
        return buildType;
    }

    public void setBuildtype(String buildType) {
        this.buildType = buildType;
    }

    public List<releng_Criterion> getReleng_criterions() {
        return releng_criterions;
    }

    public void addReleng_criterion(Releng_criterion releng_criterion) {
        this.releng_criterions.add(releng_criterion);
    }
    public releng_BuildJob getReleng_buildjob() {
        return releng_buildjob;
    }

    public void setReleng_buildjob(releng_BuildJob releng_buildjob) {
        this.releng_buildjob = releng_buildjob;
    }
    public releng_Repository getReleng_repository() {
        return releng_repository;
    }

    public void setReleng_repository(releng_Repository releng_repository) {
        this.releng_repository = releng_repository;
    }
    public releng_BuildJob getReleng_buildjob() {
        return releng_buildjob;
    }

    public void setReleng_buildjob(releng_BuildJob releng_buildjob) {
        this.releng_buildjob = releng_buildjob;
    }

}