





import java.util.List;
import java.util.ArrayList;

public class myAtl_NameExpCS extends IndexExpCS {

    private String element;
    private String namespace;



    public myAtl_NameExpCS(
        String element,        String namespace    ) {
        super(
        );
        this.element = element;
        this.namespace = namespace;
    }


    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }


}