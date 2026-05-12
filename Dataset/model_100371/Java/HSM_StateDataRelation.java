





import java.util.List;
import java.util.ArrayList;

public class HSM_StateDataRelation extends PrimitiveState {

    private String color;
    private String value;





    private OrState orstate;




    private AssociationDataStateBase associationdatastatebase;


    public HSM_StateDataRelation(
        String color,        String value    ) {
        super(
        );
        this.color = color;
        this.value = value;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public OrState getOrstate() {
        return orstate;
    }

    public void setOrstate(OrState orstate) {
        this.orstate = orstate;
    }
    public AssociationDataStateBase getAssociationdatastatebase() {
        return associationdatastatebase;
    }

    public void setAssociationdatastatebase(AssociationDataStateBase associationdatastatebase) {
        this.associationdatastatebase = associationdatastatebase;
    }

}