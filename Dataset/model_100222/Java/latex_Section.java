





import java.util.List;
import java.util.ArrayList;

public class latex_Section  {

    private String sectiontext;
    private String sectionname;
    private String sectionprefix;





    private latex_Body latex_body;




    private List<latex_General> latex_generals;


    public latex_Section(
        String sectiontext,        String sectionname,        String sectionprefix    ) {
        this.sectiontext = sectiontext;
        this.sectionname = sectionname;
        this.sectionprefix = sectionprefix;
        this.latex_generals = new ArrayList<>();
    }

    public latex_Section(
        String sectiontext,        String sectionname,        String sectionprefix        ArrayList<latex_General> latex_generals    ) {
        this.sectiontext = sectiontext;
        this.sectionname = sectionname;
        this.sectionprefix = sectionprefix;
        this.latex_generals = latex_generals;
    }

    public String getSectiontext() {
        return sectiontext;
    }

    public void setSectiontext(String sectiontext) {
        this.sectiontext = sectiontext;
    }
    public String getSectionname() {
        return sectionname;
    }

    public void setSectionname(String sectionname) {
        this.sectionname = sectionname;
    }
    public String getSectionprefix() {
        return sectionprefix;
    }

    public void setSectionprefix(String sectionprefix) {
        this.sectionprefix = sectionprefix;
    }

    public latex_Body getLatex_body() {
        return latex_body;
    }

    public void setLatex_body(latex_Body latex_body) {
        this.latex_body = latex_body;
    }
    public List<latex_General> getLatex_generals() {
        return latex_generals;
    }

    public void addLatex_general(Latex_general latex_general) {
        this.latex_generals.add(latex_general);
    }

}