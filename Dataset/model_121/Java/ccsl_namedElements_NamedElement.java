





import java.util.List;
import java.util.ArrayList;

public class ccsl_namedElements_NamedElement extends Element {

    private String avaliableInSourceCode;
    private String name;



    public ccsl_namedElements_NamedElement(
        String avaliableInSourceCode,        String name    ) {
        super(
        );
        this.avaliableInSourceCode = avaliableInSourceCode;
        this.name = name;
    }


    public String getAvaliableinsourcecode() {
        return avaliableInSourceCode;
    }

    public void setAvaliableinsourcecode(String avaliableInSourceCode) {
        this.avaliableInSourceCode = avaliableInSourceCode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}