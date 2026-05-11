





import java.util.List;
import java.util.ArrayList;

public class type_Assosiation extends Relationship {

    private String targetOperation;
    private boolean internal;
    private String sourceOperation;
    private String type;
    private String containment;



    public type_Assosiation(
        String targetOperation,        boolean internal,        String sourceOperation,        String type,        String containment    ) {
        super(
        );
        this.targetOperation = targetOperation;
        this.internal = internal;
        this.sourceOperation = sourceOperation;
        this.type = type;
        this.containment = containment;
    }


    public String getTargetoperation() {
        return targetOperation;
    }

    public void setTargetoperation(String targetOperation) {
        this.targetOperation = targetOperation;
    }
    public boolean getInternal() {
        return internal;
    }

    public void setInternal(boolean internal) {
        this.internal = internal;
    }
    public String getSourceoperation() {
        return sourceOperation;
    }

    public void setSourceoperation(String sourceOperation) {
        this.sourceOperation = sourceOperation;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getContainment() {
        return containment;
    }

    public void setContainment(String containment) {
        this.containment = containment;
    }


}