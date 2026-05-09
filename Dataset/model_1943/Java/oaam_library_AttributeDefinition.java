





import java.util.List;
import java.util.ArrayList;

public class oaam_library_AttributeDefinition extends OaamBaseElementA {

    private String target;
    private String dataType;



    public oaam_library_AttributeDefinition(
        String target,        String dataType    ) {
        super(
        );
        this.target = target;
        this.dataType = dataType;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }


}