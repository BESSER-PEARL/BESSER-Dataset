





import java.util.List;
import java.util.ArrayList;

public class avm_Formula extends ValueNode {

    private String XPosition;
    private String YPosition;
    private String Name;





    private avm_Component avm_component;


    public avm_Formula(
        String XPosition,        String YPosition,        String Name    ) {
        super(
        );
        this.XPosition = XPosition;
        this.YPosition = YPosition;
        this.Name = Name;
    }


    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}