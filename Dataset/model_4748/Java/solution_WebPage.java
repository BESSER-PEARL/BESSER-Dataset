





import java.util.List;
import java.util.ArrayList;

public class solution_WebPage  {

    private String relativeUrl;
    private String name;





    private solution_WebApplication solution_webapplication;


    public solution_WebPage(
        String relativeUrl,        String name    ) {
        this.relativeUrl = relativeUrl;
        this.name = name;
    }


    public String getRelativeurl() {
        return relativeUrl;
    }

    public void setRelativeurl(String relativeUrl) {
        this.relativeUrl = relativeUrl;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public solution_WebApplication getSolution_webapplication() {
        return solution_webapplication;
    }

    public void setSolution_webapplication(solution_WebApplication solution_webapplication) {
        this.solution_webapplication = solution_webapplication;
    }

}