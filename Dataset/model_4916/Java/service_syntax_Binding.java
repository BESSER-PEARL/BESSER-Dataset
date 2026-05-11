





import java.util.List;
import java.util.ArrayList;

public class service_syntax_Binding  {

    private String style;
    private String transport;
    private String name;





    private InterfaceDescription interfacedescription;


    public service_syntax_Binding(
        String style,        String transport,        String name    ) {
        this.style = style;
        this.transport = transport;
        this.name = name;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getTransport() {
        return transport;
    }

    public void setTransport(String transport) {
        this.transport = transport;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public InterfaceDescription getInterfacedescription() {
        return interfacedescription;
    }

    public void setInterfacedescription(InterfaceDescription interfacedescription) {
        this.interfacedescription = interfacedescription;
    }

}