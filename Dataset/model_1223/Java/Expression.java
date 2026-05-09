





import java.util.List;
import java.util.ArrayList;

public class Expression  {






    private express_instances_Constant express_instances_constant;




    private express_expressions_Selector express_expressions_selector;




    private express_expressions_IndexOperation express_expressions_indexoperation;




    private express_algorithms_LocalVariable express_algorithms_localvariable;




    private express_rules_SubtypeConstraint express_rules_subtypeconstraint;


    public Expression(
    ) {
    }



    public express_instances_Constant getExpress_instances_constant() {
        return express_instances_constant;
    }

    public void setExpress_instances_constant(express_instances_Constant express_instances_constant) {
        this.express_instances_constant = express_instances_constant;
    }
    public express_expressions_Selector getExpress_expressions_selector() {
        return express_expressions_selector;
    }

    public void setExpress_expressions_selector(express_expressions_Selector express_expressions_selector) {
        this.express_expressions_selector = express_expressions_selector;
    }
    public express_expressions_IndexOperation getExpress_expressions_indexoperation() {
        return express_expressions_indexoperation;
    }

    public void setExpress_expressions_indexoperation(express_expressions_IndexOperation express_expressions_indexoperation) {
        this.express_expressions_indexoperation = express_expressions_indexoperation;
    }
    public express_algorithms_LocalVariable getExpress_algorithms_localvariable() {
        return express_algorithms_localvariable;
    }

    public void setExpress_algorithms_localvariable(express_algorithms_LocalVariable express_algorithms_localvariable) {
        this.express_algorithms_localvariable = express_algorithms_localvariable;
    }
    public express_rules_SubtypeConstraint getExpress_rules_subtypeconstraint() {
        return express_rules_subtypeconstraint;
    }

    public void setExpress_rules_subtypeconstraint(express_rules_SubtypeConstraint express_rules_subtypeconstraint) {
        this.express_rules_subtypeconstraint = express_rules_subtypeconstraint;
    }

}