





import java.util.List;
import java.util.ArrayList;

public class sedml_model  {

    private String source;
    private String language;
    private String name;
    private String id;





    private sedml_listOfModels sedml_listofmodels;


    public sedml_model(
        String source,        String language,        String name,        String id    ) {
        this.source = source;
        this.language = language;
        this.name = name;
        this.id = id;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public sedml_listOfModels getSedml_listofmodels() {
        return sedml_listofmodels;
    }

    public void setSedml_listofmodels(sedml_listOfModels sedml_listofmodels) {
        this.sedml_listofmodels = sedml_listofmodels;
    }

}