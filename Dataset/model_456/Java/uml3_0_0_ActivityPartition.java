





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ActivityPartition extends NamedElement, ActivityGroup {

    private String isExternal;
    private String isDimension;





    private List<uml3_0_0_ActivityPartition> uml3_0_0_activitypartitions;




    private uml3_0_0_ActivityPartition uml3_0_0_activitypartition;




    private uml3_0_0_Element uml3_0_0_element;


    public uml3_0_0_ActivityPartition(
        String isExternal,        String isDimension    ) {
        super(
        );
        this.isExternal = isExternal;
        this.isDimension = isDimension;
        this.uml3_0_0_activitypartitions = new ArrayList<>();
    }

    public uml3_0_0_ActivityPartition(
        String isExternal,        String isDimension        ArrayList<uml3_0_0_ActivityPartition> uml3_0_0_activitypartitions    ) {
        this.isExternal = isExternal;
        this.isDimension = isDimension;
        this.uml3_0_0_activitypartitions = uml3_0_0_activitypartitions;
    }

    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }
    public String getIsdimension() {
        return isDimension;
    }

    public void setIsdimension(String isDimension) {
        this.isDimension = isDimension;
    }

    public List<uml3_0_0_ActivityPartition> getUml3_0_0_activitypartitions() {
        return uml3_0_0_activitypartitions;
    }

    public void addUml3_0_0_activitypartition(Uml3_0_0_activitypartition uml3_0_0_activitypartition) {
        this.uml3_0_0_activitypartitions.add(uml3_0_0_activitypartition);
    }
    public uml3_0_0_ActivityPartition getUml3_0_0_activitypartition() {
        return uml3_0_0_activitypartition;
    }

    public void setUml3_0_0_activitypartition(uml3_0_0_ActivityPartition uml3_0_0_activitypartition) {
        this.uml3_0_0_activitypartition = uml3_0_0_activitypartition;
    }
    public uml3_0_0_Element getUml3_0_0_element() {
        return uml3_0_0_element;
    }

    public void setUml3_0_0_element(uml3_0_0_Element uml3_0_0_element) {
        this.uml3_0_0_element = uml3_0_0_element;
    }

}