





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_DataType extends Classifier {






    private List<RefOntoUML_Property> refontouml_propertys;




    private RefOntoUML_Property refontouml_property;


    public RefOntoUML_DataType(
    ) {
        super(
        );
        this.refontouml_propertys = new ArrayList<>();
    }

    public RefOntoUML_DataType(
        ArrayList<RefOntoUML_Property> refontouml_propertys    ) {
        this.refontouml_propertys = refontouml_propertys;
    }


    public List<RefOntoUML_Property> getRefontouml_propertys() {
        return refontouml_propertys;
    }

    public void addRefontouml_property(Refontouml_property refontouml_property) {
        this.refontouml_propertys.add(refontouml_property);
    }
    public RefOntoUML_Property getRefontouml_property() {
        return refontouml_property;
    }

    public void setRefontouml_property(RefOntoUML_Property refontouml_property) {
        this.refontouml_property = refontouml_property;
    }

}