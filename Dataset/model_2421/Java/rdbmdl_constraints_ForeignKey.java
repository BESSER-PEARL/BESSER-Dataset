





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_constraints_ForeignKey extends ColumnRefConstraint {






    private UniqueConstraint uniqueconstraint;


    public rdbmdl_constraints_ForeignKey(
    ) {
        super(
        );
    }



    public UniqueConstraint getUniqueconstraint() {
        return uniqueconstraint;
    }

    public void setUniqueconstraint(UniqueConstraint uniqueconstraint) {
        this.uniqueconstraint = uniqueconstraint;
    }

}