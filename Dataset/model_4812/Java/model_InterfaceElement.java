





import java.util.List;
import java.util.ArrayList;

public class model_InterfaceElement extends ZentaElement {

    private int interfaceType;



    public model_InterfaceElement(
        int interfaceType    ) {
        super(
        );
        this.interfaceType = interfaceType;
    }


    public int getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(int interfaceType) {
        this.interfaceType = interfaceType;
    }


}