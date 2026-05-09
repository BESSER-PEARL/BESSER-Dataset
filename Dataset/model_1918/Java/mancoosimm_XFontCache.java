





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_XFontCache  {

    private String location;





    private mancoosimm_Environment mancoosimm_environment;




    private mancoosimm_Environment mancoosimm_environment;




    private mancoosimm_XFont mancoosimm_xfont;




    private List<mancoosimm_XFont> mancoosimm_xfonts;


    public mancoosimm_XFontCache(
        String location    ) {
        this.location = location;
        this.mancoosimm_xfonts = new ArrayList<>();
    }

    public mancoosimm_XFontCache(
        String location        ArrayList<mancoosimm_XFont> mancoosimm_xfonts    ) {
        this.location = location;
        this.mancoosimm_xfonts = mancoosimm_xfonts;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public mancoosimm_XFont getMancoosimm_xfont() {
        return mancoosimm_xfont;
    }

    public void setMancoosimm_xfont(mancoosimm_XFont mancoosimm_xfont) {
        this.mancoosimm_xfont = mancoosimm_xfont;
    }
    public List<mancoosimm_XFont> getMancoosimm_xfonts() {
        return mancoosimm_xfonts;
    }

    public void addMancoosimm_xfont(Mancoosimm_xfont mancoosimm_xfont) {
        this.mancoosimm_xfonts.add(mancoosimm_xfont);
    }

}