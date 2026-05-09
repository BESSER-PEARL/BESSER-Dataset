





import java.util.List;
import java.util.ArrayList;

public class uma_Property extends DiagramElement {

    private String key;
    private String value;





    private uma_DiagramElement uma_diagramelement;


    public uma_Property(
        String key,        String value    ) {
        super(
        );
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public uma_DiagramElement getUma_diagramelement() {
        return uma_diagramelement;
    }

    public void setUma_diagramelement(uma_DiagramElement uma_diagramelement) {
        this.uma_diagramelement = uma_diagramelement;
    }

}