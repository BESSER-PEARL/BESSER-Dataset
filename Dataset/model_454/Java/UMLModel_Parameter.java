





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Parameter extends ConnectableElement, MultiplicityElement {

    private String default;
    private String parameterSet;
    private String operation;
    private String isStream;
    private String direction;
    private String isException;
    private String effect;





    private UMLModel_ValueSpecification umlmodel_valuespecification;


    public UMLModel_Parameter(
        String default,        String parameterSet,        String operation,        String isStream,        String direction,        String isException,        String effect    ) {
        super(
        );
        this.default = default;
        this.parameterSet = parameterSet;
        this.operation = operation;
        this.isStream = isStream;
        this.direction = direction;
        this.isException = isException;
        this.effect = effect;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getParameterset() {
        return parameterSet;
    }

    public void setParameterset(String parameterSet) {
        this.parameterSet = parameterSet;
    }
    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }
    public String getIsstream() {
        return isStream;
    }

    public void setIsstream(String isStream) {
        this.isStream = isStream;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getIsexception() {
        return isException;
    }

    public void setIsexception(String isException) {
        this.isException = isException;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }

    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }

}