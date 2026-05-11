





import java.util.List;
import java.util.ArrayList;

public class ccore_GroupOfAttributes  {

    private int column;





    private ccore_GroupOfAttributes ccore_groupofattributes;




    private List<ccore_Attribute> ccore_attributes;




    private ccore_TypeDefinition ccore_typedefinition;


    public ccore_GroupOfAttributes(
        int column    ) {
        this.column = column;
        this.ccore_attributes = new ArrayList<>();
    }

    public ccore_GroupOfAttributes(
        int column        ArrayList<ccore_Attribute> ccore_attributes    ) {
        this.column = column;
        this.ccore_attributes = ccore_attributes;
    }

    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }

    public ccore_GroupOfAttributes getCcore_groupofattributes() {
        return ccore_groupofattributes;
    }

    public void setCcore_groupofattributes(ccore_GroupOfAttributes ccore_groupofattributes) {
        this.ccore_groupofattributes = ccore_groupofattributes;
    }
    public List<ccore_Attribute> getCcore_attributes() {
        return ccore_attributes;
    }

    public void addCcore_attribute(Ccore_attribute ccore_attribute) {
        this.ccore_attributes.add(ccore_attribute);
    }
    public ccore_TypeDefinition getCcore_typedefinition() {
        return ccore_typedefinition;
    }

    public void setCcore_typedefinition(ccore_TypeDefinition ccore_typedefinition) {
        this.ccore_typedefinition = ccore_typedefinition;
    }

}