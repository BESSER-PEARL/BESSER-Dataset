





import java.util.List;
import java.util.ArrayList;

public class express_core_AggregationType  {

    private String isUnique;
    private String ordering;





    private SizeConstraint sizeconstraint;




    private SizeConstraint sizeconstraint;


    public express_core_AggregationType(
        String isUnique,        String ordering    ) {
        this.isUnique = isUnique;
        this.ordering = ordering;
    }


    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }

    public SizeConstraint getSizeconstraint() {
        return sizeconstraint;
    }

    public void setSizeconstraint(SizeConstraint sizeconstraint) {
        this.sizeconstraint = sizeconstraint;
    }
    public SizeConstraint getSizeconstraint() {
        return sizeconstraint;
    }

    public void setSizeconstraint(SizeConstraint sizeconstraint) {
        this.sizeconstraint = sizeconstraint;
    }

}