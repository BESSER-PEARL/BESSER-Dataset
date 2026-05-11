





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_Views_ElementView  {

    private String dsisplayName;
    private String description;
    private String name;



    public classLayout2Frontend_Views_ElementView(
        String dsisplayName,        String description,        String name    ) {
        this.dsisplayName = dsisplayName;
        this.description = description;
        this.name = name;
    }


    public String getDsisplayname() {
        return dsisplayName;
    }

    public void setDsisplayname(String dsisplayName) {
        this.dsisplayName = dsisplayName;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}