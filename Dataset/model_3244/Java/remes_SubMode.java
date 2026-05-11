





import java.util.List;
import java.util.ArrayList;

public class remes_SubMode extends Mode {

    private String resourceClassC;
    private String invariant;
    private String resourceClassB;
    private String isUrgent;
    private String resourceClassA;





    private remes_CompositeMode remes_compositemode;




    private remes_CompositeMode remes_compositemode;


    public remes_SubMode(
        String resourceClassC,        String invariant,        String resourceClassB,        String isUrgent,        String resourceClassA    ) {
        super(
        );
        this.resourceClassC = resourceClassC;
        this.invariant = invariant;
        this.resourceClassB = resourceClassB;
        this.isUrgent = isUrgent;
        this.resourceClassA = resourceClassA;
    }


    public String getResourceclassc() {
        return resourceClassC;
    }

    public void setResourceclassc(String resourceClassC) {
        this.resourceClassC = resourceClassC;
    }
    public String getInvariant() {
        return invariant;
    }

    public void setInvariant(String invariant) {
        this.invariant = invariant;
    }
    public String getResourceclassb() {
        return resourceClassB;
    }

    public void setResourceclassb(String resourceClassB) {
        this.resourceClassB = resourceClassB;
    }
    public String getIsurgent() {
        return isUrgent;
    }

    public void setIsurgent(String isUrgent) {
        this.isUrgent = isUrgent;
    }
    public String getResourceclassa() {
        return resourceClassA;
    }

    public void setResourceclassa(String resourceClassA) {
        this.resourceClassA = resourceClassA;
    }

    public remes_CompositeMode getRemes_compositemode() {
        return remes_compositemode;
    }

    public void setRemes_compositemode(remes_CompositeMode remes_compositemode) {
        this.remes_compositemode = remes_compositemode;
    }
    public remes_CompositeMode getRemes_compositemode() {
        return remes_compositemode;
    }

    public void setRemes_compositemode(remes_CompositeMode remes_compositemode) {
        this.remes_compositemode = remes_compositemode;
    }

}