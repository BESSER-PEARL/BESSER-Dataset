





import java.util.List;
import java.util.ArrayList;

public class model_Extension extends BPELExtensibleElement {

    private String namespace;
    private String mustUnderstand;



    public model_Extension(
        String namespace,        String mustUnderstand    ) {
        super(
        );
        this.namespace = namespace;
        this.mustUnderstand = mustUnderstand;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getMustunderstand() {
        return mustUnderstand;
    }

    public void setMustunderstand(String mustUnderstand) {
        this.mustUnderstand = mustUnderstand;
    }


}