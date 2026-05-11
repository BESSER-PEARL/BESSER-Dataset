





import java.util.List;
import java.util.ArrayList;

public class SecCon_Parameter extends MultiplicityElement, TypedElement {

    private String default;
    private String direction;





    private SecCon_Operation seccon_operation;


    public SecCon_Parameter(
        String default,        String direction    ) {
        super(
        );
        this.default = default;
        this.direction = direction;
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

    public SecCon_Operation getSeccon_operation() {
        return seccon_operation;
    }

    public void setSeccon_operation(SecCon_Operation seccon_operation) {
        this.seccon_operation = seccon_operation;
    }

}