





import java.util.List;
import java.util.ArrayList;

public class dsl_EntityName  {

    private String name;





    private dsl_Operation dsl_operation;




    private dsl_RelationDom dsl_relationdom;




    private dsl_RelationDom dsl_relationdom;


    public dsl_EntityName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Operation getDsl_operation() {
        return dsl_operation;
    }

    public void setDsl_operation(dsl_Operation dsl_operation) {
        this.dsl_operation = dsl_operation;
    }
    public dsl_RelationDom getDsl_relationdom() {
        return dsl_relationdom;
    }

    public void setDsl_relationdom(dsl_RelationDom dsl_relationdom) {
        this.dsl_relationdom = dsl_relationdom;
    }
    public dsl_RelationDom getDsl_relationdom() {
        return dsl_relationdom;
    }

    public void setDsl_relationdom(dsl_RelationDom dsl_relationdom) {
        this.dsl_relationdom = dsl_relationdom;
    }

}