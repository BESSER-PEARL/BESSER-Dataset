





import java.util.List;
import java.util.ArrayList;

public class webGui_Model  {

    private String name;





    private webGui_DomainModel webgui_domainmodel;




    private webGui_WebModel webgui_webmodel;


    public webGui_Model(
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
    public webGui_WebModel getWebgui_webmodel() {
        return webgui_webmodel;
    }

    public void setWebgui_webmodel(webGui_WebModel webgui_webmodel) {
        this.webgui_webmodel = webgui_webmodel;
    }

}