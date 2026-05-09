





import java.util.List;
import java.util.ArrayList;

public class UML2_ActivityPartition extends NamedElement, ActivityGroup {

    private boolean isDimension;
    private boolean isExternal;





    private UML2_Element uml2_element;




    private List<UML2_ActivityPartition> uml2_activitypartitions;




    private UML2_ActivityPartition uml2_activitypartition;


    public UML2_ActivityPartition(
        boolean isDimension,        boolean isExternal    ) {
        super(
        );
        this.isDimension = isDimension;
        this.isExternal = isExternal;
        this.uml2_activitypartitions = new ArrayList<>();
    }

    public UML2_ActivityPartition(
        boolean isDimension,        boolean isExternal        ArrayList<UML2_ActivityPartition> uml2_activitypartitions    ) {
        this.isDimension = isDimension;
        this.isExternal = isExternal;
        this.uml2_activitypartitions = uml2_activitypartitions;
    }

    public boolean getIsdimension() {
        return isDimension;
    }

    public void setIsdimension(boolean isDimension) {
        this.isDimension = isDimension;
    }
    public boolean getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(boolean isExternal) {
        this.isExternal = isExternal;
    }

    public UML2_Element getUml2_element() {
        return uml2_element;
    }

    public void setUml2_element(UML2_Element uml2_element) {
        this.uml2_element = uml2_element;
    }
    public List<UML2_ActivityPartition> getUml2_activitypartitions() {
        return uml2_activitypartitions;
    }

    public void addUml2_activitypartition(Uml2_activitypartition uml2_activitypartition) {
        this.uml2_activitypartitions.add(uml2_activitypartition);
    }
    public UML2_ActivityPartition getUml2_activitypartition() {
        return uml2_activitypartition;
    }

    public void setUml2_activitypartition(UML2_ActivityPartition uml2_activitypartition) {
        this.uml2_activitypartition = uml2_activitypartition;
    }

}