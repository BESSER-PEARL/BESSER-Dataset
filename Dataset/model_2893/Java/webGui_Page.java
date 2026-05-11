





import java.util.List;
import java.util.ArrayList;

public class webGui_Page  {

    private String title;
    private String name;





    private webGui_Entity webgui_entity;




    private webGui_WebModel webgui_webmodel;


    public webGui_Page(
        String title,        String name    ) {
        this.title = title;
        this.name = name;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public webGui_Entity getWebgui_entity() {
        return webgui_entity;
    }

    public void setWebgui_entity(webGui_Entity webgui_entity) {
        this.webgui_entity = webgui_entity;
    }
    public webGui_WebModel getWebgui_webmodel() {
        return webgui_webmodel;
    }

    public void setWebgui_webmodel(webGui_WebModel webgui_webmodel) {
        this.webgui_webmodel = webgui_webmodel;
    }

}