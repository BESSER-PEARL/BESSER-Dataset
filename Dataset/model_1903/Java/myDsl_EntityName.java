





import java.util.List;
import java.util.ArrayList;

public class myDsl_EntityName  {

    private String name;





    private myDsl_RelationDom mydsl_relationdom;




    private myDsl_Operation mydsl_operation;




    private myDsl_RelationDom mydsl_relationdom;


    public myDsl_EntityName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_RelationDom getMydsl_relationdom() {
        return mydsl_relationdom;
    }

    public void setMydsl_relationdom(myDsl_RelationDom mydsl_relationdom) {
        this.mydsl_relationdom = mydsl_relationdom;
    }
    public myDsl_Operation getMydsl_operation() {
        return mydsl_operation;
    }

    public void setMydsl_operation(myDsl_Operation mydsl_operation) {
        this.mydsl_operation = mydsl_operation;
    }
    public myDsl_RelationDom getMydsl_relationdom() {
        return mydsl_relationdom;
    }

    public void setMydsl_relationdom(myDsl_RelationDom mydsl_relationdom) {
        this.mydsl_relationdom = mydsl_relationdom;
    }

}