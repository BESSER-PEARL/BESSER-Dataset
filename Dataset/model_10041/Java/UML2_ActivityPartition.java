





import java.util.List;
import java.util.ArrayList;

public class UML2_ActivityPartition extends NamedElement, ActivityGroup {

    private boolean isExternal;
    private boolean isDimension;





    private UML2_Element uml2_element;




    private UML2_ActivityPartition uml2_activitypartition;




    private List<UML2_ActivityPartition> uml2_activitypartitions;


    public UML2_ActivityPartition(
        boolean isExternal,        boolean isDimension    ) {
        super(
        );
        this.isExternal = isExternal;
        this.isDimension = isDimension;
        this.uml2_activitypartitions = new ArrayList<>();
    }

    public UML2_ActivityPartition(
        boolean isExternal,        boolean isDimension        ArrayList<UML2_ActivityPartition> uml2_activitypartitions    ) {
        this.isExternal = isExternal;
        this.isDimension = isDimension;
        this.uml2_activitypartitions = uml2_activitypartitions;
    }

    public boolean getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(boolean isExternal) {
        this.isExternal = isExternal;
    }
    public boolean getIsdimension() {
        return isDimension;
    }

    public void setIsdimension(boolean isDimension) {
        this.isDimension = isDimension;
    }

    public UML2_Element getUml2_element() {
        return uml2_element;
    }

    public void setUml2_element(UML2_Element uml2_element) {
        this.uml2_element = uml2_element;
    }
    public UML2_ActivityPartition getUml2_activitypartition() {
        return uml2_activitypartition;
    }

    public void setUml2_activitypartition(UML2_ActivityPartition uml2_activitypartition) {
        this.uml2_activitypartition = uml2_activitypartition;
    }
    public List<UML2_ActivityPartition> getUml2_activitypartitions() {
        return uml2_activitypartitions;
    }

    public void addUml2_activitypartition(Uml2_activitypartition uml2_activitypartition) {
        this.uml2_activitypartitions.add(uml2_activitypartition);
    }

}