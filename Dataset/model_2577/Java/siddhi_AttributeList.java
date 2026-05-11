





import java.util.List;
import java.util.ArrayList;

public class siddhi_AttributeList  {






    private siddhi_FunctionOperation siddhi_functionoperation;




    private List<siddhi_Attribute> siddhi_attributes;


    public siddhi_AttributeList(
    ) {
        this.siddhi_attributes = new ArrayList<>();
    }

    public siddhi_AttributeList(
        ArrayList<siddhi_Attribute> siddhi_attributes    ) {
        this.siddhi_attributes = siddhi_attributes;
    }


    public siddhi_FunctionOperation getSiddhi_functionoperation() {
        return siddhi_functionoperation;
    }

    public void setSiddhi_functionoperation(siddhi_FunctionOperation siddhi_functionoperation) {
        this.siddhi_functionoperation = siddhi_functionoperation;
    }
    public List<siddhi_Attribute> getSiddhi_attributes() {
        return siddhi_attributes;
    }

    public void addSiddhi_attribute(Siddhi_attribute siddhi_attribute) {
        this.siddhi_attributes.add(siddhi_attribute);
    }

}