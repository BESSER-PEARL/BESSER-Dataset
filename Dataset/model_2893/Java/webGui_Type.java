





import java.util.List;
import java.util.ArrayList;

public class webGui_Type  {

    private String name;





    private webGui_DomainModel webgui_domainmodel;


    public webGui_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public webGui_DomainModel getWebgui_domainmodel() {
        return webgui_domainmodel;
    }

    public void setWebgui_domainmodel(webGui_DomainModel webgui_domainmodel) {
        this.webgui_domainmodel = webgui_domainmodel;
    }

}