





import java.util.List;
import java.util.ArrayList;

public class express_core_Redeclaration  {

    private String position;
    private String isMandatory;





    private EntityType entitytype;




    private Expression expression;




    private Attribute attribute;




    private SizeConstraint sizeconstraint;




    private SizeConstraint sizeconstraint;




    private ScopedId scopedid;


    public express_core_Redeclaration(
        String position,        String isMandatory    ) {
        this.position = position;
        this.isMandatory = isMandatory;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(String isMandatory) {
        this.isMandatory = isMandatory;
    }

    public EntityType getEntitytype() {
        return entitytype;
    }

    public void setEntitytype(EntityType entitytype) {
        this.entitytype = entitytype;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public Attribute getAttribute() {
        return attribute;
    }

    public void setAttribute(Attribute attribute) {
        this.attribute = attribute;
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
    public ScopedId getScopedid() {
        return scopedid;
    }

    public void setScopedid(ScopedId scopedid) {
        this.scopedid = scopedid;
    }

}