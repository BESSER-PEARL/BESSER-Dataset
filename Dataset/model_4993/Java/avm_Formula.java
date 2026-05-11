





import java.util.List;
import java.util.ArrayList;

public class avm_Formula extends ValueNode {

    private String XPosition;
    private String Name;
    private String YPosition;





    private avm_Container avm_container;




    private avm_Component avm_component;


    public avm_Formula(
        String XPosition,        String Name,        String YPosition    ) {
        super(
        );
        this.XPosition = XPosition;
        this.Name = Name;
        this.YPosition = YPosition;
    }


    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }

    public avm_Container getAvm_container() {
        return avm_container;
    }

    public void setAvm_container(avm_Container avm_container) {
        this.avm_container = avm_container;
    }
    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}