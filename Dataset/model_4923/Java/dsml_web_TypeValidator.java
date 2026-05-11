





import java.util.List;
import java.util.ArrayList;

public class dsml_web_TypeValidator extends Validator {

    private String type;



    public dsml_web_TypeValidator(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}