





import java.util.List;
import java.util.ArrayList;

public class sparqlas_ObjectPropertyExpression extends Expression {






    private sparqlas_ObjectMinCardinality sparqlas_objectmincardinality;




    private sparqlas_ObjectExactCardinality sparqlas_objectexactcardinality;




    private sparqlas_ObjectSomeValuesFrom sparqlas_objectsomevaluesfrom;




    private sparqlas_ObjectMaxCardinality sparqlas_objectmaxcardinality;




    private sparqlas_ObjectPropertyAssertion sparqlas_objectpropertyassertion;




    private sparqlas_ObjectAllValuesFrom sparqlas_objectallvaluesfrom;




    private sparqlas_ObjectHasValue sparqlas_objecthasvalue;




    private sparqlas_InverseObjectProperty sparqlas_inverseobjectproperty;


    public sparqlas_ObjectPropertyExpression(
    ) {
        super(
        );
    }



    public sparqlas_ObjectMinCardinality getSparqlas_objectmincardinality() {
        return sparqlas_objectmincardinality;
    }

    public void setSparqlas_objectmincardinality(sparqlas_ObjectMinCardinality sparqlas_objectmincardinality) {
        this.sparqlas_objectmincardinality = sparqlas_objectmincardinality;
    }
    public sparqlas_ObjectExactCardinality getSparqlas_objectexactcardinality() {
        return sparqlas_objectexactcardinality;
    }

    public void setSparqlas_objectexactcardinality(sparqlas_ObjectExactCardinality sparqlas_objectexactcardinality) {
        this.sparqlas_objectexactcardinality = sparqlas_objectexactcardinality;
    }
    public sparqlas_ObjectSomeValuesFrom getSparqlas_objectsomevaluesfrom() {
        return sparqlas_objectsomevaluesfrom;
    }

    public void setSparqlas_objectsomevaluesfrom(sparqlas_ObjectSomeValuesFrom sparqlas_objectsomevaluesfrom) {
        this.sparqlas_objectsomevaluesfrom = sparqlas_objectsomevaluesfrom;
    }
    public sparqlas_ObjectMaxCardinality getSparqlas_objectmaxcardinality() {
        return sparqlas_objectmaxcardinality;
    }

    public void setSparqlas_objectmaxcardinality(sparqlas_ObjectMaxCardinality sparqlas_objectmaxcardinality) {
        this.sparqlas_objectmaxcardinality = sparqlas_objectmaxcardinality;
    }
    public sparqlas_ObjectPropertyAssertion getSparqlas_objectpropertyassertion() {
        return sparqlas_objectpropertyassertion;
    }

    public void setSparqlas_objectpropertyassertion(sparqlas_ObjectPropertyAssertion sparqlas_objectpropertyassertion) {
        this.sparqlas_objectpropertyassertion = sparqlas_objectpropertyassertion;
    }
    public sparqlas_ObjectAllValuesFrom getSparqlas_objectallvaluesfrom() {
        return sparqlas_objectallvaluesfrom;
    }

    public void setSparqlas_objectallvaluesfrom(sparqlas_ObjectAllValuesFrom sparqlas_objectallvaluesfrom) {
        this.sparqlas_objectallvaluesfrom = sparqlas_objectallvaluesfrom;
    }
    public sparqlas_ObjectHasValue getSparqlas_objecthasvalue() {
        return sparqlas_objecthasvalue;
    }

    public void setSparqlas_objecthasvalue(sparqlas_ObjectHasValue sparqlas_objecthasvalue) {
        this.sparqlas_objecthasvalue = sparqlas_objecthasvalue;
    }
    public sparqlas_InverseObjectProperty getSparqlas_inverseobjectproperty() {
        return sparqlas_inverseobjectproperty;
    }

    public void setSparqlas_inverseobjectproperty(sparqlas_InverseObjectProperty sparqlas_inverseobjectproperty) {
        this.sparqlas_inverseobjectproperty = sparqlas_inverseobjectproperty;
    }

}