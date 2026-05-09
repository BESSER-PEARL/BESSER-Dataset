





import java.util.List;
import java.util.ArrayList;

public class express_algorithms_ActualGenericType extends ActualType {

    private String label;
    private String isEntity;





    private ActualDataType actualdatatype;


    public express_algorithms_ActualGenericType(
        String label,        String isEntity    ) {
        super(
        );
        this.label = label;
        this.isEntity = isEntity;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getIsentity() {
        return isEntity;
    }

    public void setIsentity(String isEntity) {
        this.isEntity = isEntity;
    }

    public ActualDataType getActualdatatype() {
        return actualdatatype;
    }

    public void setActualdatatype(ActualDataType actualdatatype) {
        this.actualdatatype = actualdatatype;
    }

}