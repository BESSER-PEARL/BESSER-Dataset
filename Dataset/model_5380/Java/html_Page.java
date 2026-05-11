





import java.util.List;
import java.util.ArrayList;

public class html_Page  {

    private String urlToGetRelationResult;
    private String title;
    private String urlToSaveResponses;
    private String description;
    private String urlToGetData;
    private int id;





    private html_Container html_container;




    private List<html_View> html_views;


    public html_Page(
        String urlToGetRelationResult,        String title,        String urlToSaveResponses,        String description,        String urlToGetData,        int id    ) {
        this.urlToGetRelationResult = urlToGetRelationResult;
        this.title = title;
        this.urlToSaveResponses = urlToSaveResponses;
        this.description = description;
        this.urlToGetData = urlToGetData;
        this.id = id;
        this.html_views = new ArrayList<>();
    }

    public html_Page(
        String urlToGetRelationResult,        String title,        String urlToSaveResponses,        String description,        String urlToGetData,        int id        ArrayList<html_View> html_views    ) {
        this.urlToGetRelationResult = urlToGetRelationResult;
        this.title = title;
        this.urlToSaveResponses = urlToSaveResponses;
        this.description = description;
        this.urlToGetData = urlToGetData;
        this.id = id;
        this.html_views = html_views;
    }

    public String getUrltogetrelationresult() {
        return urlToGetRelationResult;
    }

    public void setUrltogetrelationresult(String urlToGetRelationResult) {
        this.urlToGetRelationResult = urlToGetRelationResult;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getUrltosaveresponses() {
        return urlToSaveResponses;
    }

    public void setUrltosaveresponses(String urlToSaveResponses) {
        this.urlToSaveResponses = urlToSaveResponses;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getUrltogetdata() {
        return urlToGetData;
    }

    public void setUrltogetdata(String urlToGetData) {
        this.urlToGetData = urlToGetData;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public html_Container getHtml_container() {
        return html_container;
    }

    public void setHtml_container(html_Container html_container) {
        this.html_container = html_container;
    }
    public List<html_View> getHtml_views() {
        return html_views;
    }

    public void addHtml_view(Html_view html_view) {
        this.html_views.add(html_view);
    }

}