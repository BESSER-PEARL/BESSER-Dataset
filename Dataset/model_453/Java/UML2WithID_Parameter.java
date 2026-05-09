





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Parameter extends MultiplicityElement, TypedElement, ConnectableElement {

    private String effect;
    private boolean isException;
    private String direction;
    private String default;
    private boolean isStream;





    private UML2WithID_OpaqueExpression uml2withid_opaqueexpression;




    private UML2WithID_ValueSpecification uml2withid_valuespecification;


    public UML2WithID_Parameter(
        String effect,        boolean isException,        String direction,        String default,        boolean isStream    ) {
        super(
        );
        this.effect = effect;
        this.isException = isException;
        this.direction = direction;
        this.default = default;
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
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getIsstream() {
        return isStream;
    }

    public void setIsstream(boolean isStream) {
        this.isStream = isStream;
    }

    public UML2WithID_OpaqueExpression getUml2withid_opaqueexpression() {
        return uml2withid_opaqueexpression;
    }

    public void setUml2withid_opaqueexpression(UML2WithID_OpaqueExpression uml2withid_opaqueexpression) {
        this.uml2withid_opaqueexpression = uml2withid_opaqueexpression;
    }
    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }

}