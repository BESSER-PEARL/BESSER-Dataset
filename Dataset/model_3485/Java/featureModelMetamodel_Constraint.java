





import java.util.List;
import java.util.ArrayList;

public class featureModelMetamodel_Constraint  {

    private String language;
    private String code;
    private String id;



    public featureModelMetamodel_Constraint(
        String language,        String code,        String id    ) {
        this.language = language;
        this.code = code;
        this.id = id;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}