





import java.util.List;
import java.util.ArrayList;

public class featuremodel_Rule  {

    private String language;
    private String code;



    public featuremodel_Rule(
        String language,        String code    ) {
        this.language = language;
        this.code = code;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}