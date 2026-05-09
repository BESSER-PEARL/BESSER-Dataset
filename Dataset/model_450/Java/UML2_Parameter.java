





import java.util.List;
import java.util.ArrayList;

public class UML2_Parameter extends TypedElement, MultiplicityElement, ConnectableElement {

    private String effect;
    private boolean isException;
    private String default;
    private String direction;
    private boolean isStream;





    private UML2_Operation uml2_operation;




    private UML2_Operation uml2_operation;


    public UML2_Parameter(
        String effect,        boolean isException,        String default,        String direction,        boolean isStream    ) {
        super(
        );
        this.effect = effect;
        this.isException = isException;
        this.default = default;
        this.direction = direction;
        this.isStream = isStream;
    }


    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public boolean getIsexception() {
        return isException;
    }

    public void setIsexception(boolean isException) {
        this.isException = isException;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public boolean getIsstream() {
        return isStream;
    }

    public void setIsstream(boolean isStream) {
        this.isStream = isStream;
    }

    public UML2_Operation getUml2_operation() {
        return uml2_operation;
    }

    public void setUml2_operation(UML2_Operation uml2_operation) {
        this.uml2_operation = uml2_operation;
    }
    public UML2_Operation getUml2_operation() {
        return uml2_operation;
    }

    public void setUml2_operation(UML2_Operation uml2_operation) {
        this.uml2_operation = uml2_operation;
    }

}