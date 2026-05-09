





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_TextValueType extends ValueType {

    private String value;



    public QualityMetamodel_TextValueType(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}