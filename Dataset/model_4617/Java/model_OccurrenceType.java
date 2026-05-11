





import java.util.List;
import java.util.ArrayList;

public class model_OccurrenceType extends AbstractRegExpTopicType, AbstractUniqueValueTopicType, ScopedReifiableTopicType, ScopedTopicType {

    private String dataType;



    public model_OccurrenceType(
        String dataType    ) {
        super(
        );
        this.dataType = dataType;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }


}