





import java.util.List;
import java.util.ArrayList;

public class solution_WebPage  {

    private String relativeUrl;
    private String name;





    private solution_WebApplication solution_webapplication;




    private List<solution_Link> solution_links;




    private solution_NonContextualLink solution_noncontextuallink;




    private solution_Link solution_link;


    public solution_WebPage(
        String relativeUrl,        String name    ) {
        this.relativeUrl = relativeUrl;
        this.name = name;
        this.solution_links = new ArrayList<>();
    }

    public solution_WebPage(
        String relativeUrl,        String name        ArrayList<solution_Link> solution_links    ) {
        this.relativeUrl = relativeUrl;
        this.name = name;
        this.solution_links = solution_links;
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
    public List<solution_Link> getSolution_links() {
        return solution_links;
    }

    public void addSolution_link(Solution_link solution_link) {
        this.solution_links.add(solution_link);
    }
    public solution_NonContextualLink getSolution_noncontextuallink() {
        return solution_noncontextuallink;
    }

    public void setSolution_noncontextuallink(solution_NonContextualLink solution_noncontextuallink) {
        this.solution_noncontextuallink = solution_noncontextuallink;
    }
    public solution_Link getSolution_link() {
        return solution_link;
    }

    public void setSolution_link(solution_Link solution_link) {
        this.solution_link = solution_link;
    }

}