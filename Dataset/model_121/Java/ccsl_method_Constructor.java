





import java.util.List;
import java.util.ArrayList;

public class ccsl_method_Constructor extends SimpleMethod {

    private String avaliableInSourceCode;



    public ccsl_method_Constructor(
        String avaliableInSourceCode    ) {
        super(
        );
        this.avaliableInSourceCode = avaliableInSourceCode;
    }


    public String getAvaliableinsourcecode() {
        return avaliableInSourceCode;
    }

    public void setAvaliableinsourcecode(String avaliableInSourceCode) {
        this.avaliableInSourceCode = avaliableInSourceCode;
    }


}