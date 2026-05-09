





import java.util.List;
import java.util.ArrayList;

public class pivot_LanguageExpression extends ValueSpecification {

    private String language;
    private String body;





    private pivot_InstanceSpecification pivot_instancespecification;




    private pivot_Constraint pivot_constraint;




    private pivot_Constraint pivot_constraint;




    private pivot_Operation pivot_operation;




    private pivot_Property pivot_property;


    public pivot_LanguageExpression(
        String language,        String body    ) {
        super(
        );
        this.language = language;
        this.body = body;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public pivot_InstanceSpecification getPivot_instancespecification() {
        return pivot_instancespecification;
    }

    public void setPivot_instancespecification(pivot_InstanceSpecification pivot_instancespecification) {
        this.pivot_instancespecification = pivot_instancespecification;
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }

}