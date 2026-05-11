





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertyExpression extends Element {






    private aadl2_Property aadl2_property;




    private aadl2_ModalPropertyValue aadl2_modalpropertyvalue;




    private aadl2_PropertyConstant aadl2_propertyconstant;


    public aadl2_PropertyExpression(
    ) {
        super(
        );
    }



    public aadl2_Property getAadl2_property() {
        return aadl2_property;
    }

    public void setAadl2_property(aadl2_Property aadl2_property) {
        this.aadl2_property = aadl2_property;
    }
    public aadl2_ModalPropertyValue getAadl2_modalpropertyvalue() {
        return aadl2_modalpropertyvalue;
    }

    public void setAadl2_modalpropertyvalue(aadl2_ModalPropertyValue aadl2_modalpropertyvalue) {
        this.aadl2_modalpropertyvalue = aadl2_modalpropertyvalue;
    }
    public aadl2_PropertyConstant getAadl2_propertyconstant() {
        return aadl2_propertyconstant;
    }

    public void setAadl2_propertyconstant(aadl2_PropertyConstant aadl2_propertyconstant) {
        this.aadl2_propertyconstant = aadl2_propertyconstant;
    }

}