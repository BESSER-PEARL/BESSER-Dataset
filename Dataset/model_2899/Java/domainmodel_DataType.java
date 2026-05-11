





import java.util.List;
import java.util.ArrayList;

public class domainmodel_DataType extends Type, AbstractNamespaceElement {

    private String name;
    private String initValue;
    private String mappedType;



    public domainmodel_DataType(
        String name,        String initValue,        String mappedType    ) {
        super(
        );
        this.name = name;
        this.initValue = initValue;
        this.mappedType = mappedType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInitvalue() {
        return initValue;
    }

    public void setInitvalue(String initValue) {
        this.initValue = initValue;
    }
    public String getMappedtype() {
        return mappedType;
    }

    public void setMappedtype(String mappedType) {
        this.mappedType = mappedType;
    }


}