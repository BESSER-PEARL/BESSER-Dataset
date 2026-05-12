





import java.util.List;
import java.util.ArrayList;

public class latex_Subsection  {

    private String subsectiontext;
    private String subsectionname;
    private String subsectionprefix;





    private List<latex_General> latex_generals;




    private latex_Subsection latex_subsection;




    private latex_Section latex_section;


    public latex_Subsection(
        String subsectiontext,        String subsectionname,        String subsectionprefix    ) {
        this.subsectiontext = subsectiontext;
        this.subsectionname = subsectionname;
        this.subsectionprefix = subsectionprefix;
        this.latex_generals = new ArrayList<>();
    }

    public latex_Subsection(
        String subsectiontext,        String subsectionname,        String subsectionprefix        ArrayList<latex_General> latex_generals    ) {
        this.subsectiontext = subsectiontext;
        this.subsectionname = subsectionname;
        this.subsectionprefix = subsectionprefix;
        this.latex_generals = latex_generals;
    }

    public String getSubsectiontext() {
        return subsectiontext;
    }

    public void setSubsectiontext(String subsectiontext) {
        this.subsectiontext = subsectiontext;
    }
    public String getSubsectionname() {
        return subsectionname;
    }

    public void setSubsectionname(String subsectionname) {
        this.subsectionname = subsectionname;
    }
    public String getSubsectionprefix() {
        return subsectionprefix;
    }

    public void setSubsectionprefix(String subsectionprefix) {
        this.subsectionprefix = subsectionprefix;
    }

    public List<latex_General> getLatex_generals() {
        return latex_generals;
    }

    public void addLatex_general(Latex_general latex_general) {
        this.latex_generals.add(latex_general);
    }
    public latex_Subsection getLatex_subsection() {
        return latex_subsection;
    }

    public void setLatex_subsection(latex_Subsection latex_subsection) {
        this.latex_subsection = latex_subsection;
    }
    public latex_Section getLatex_section() {
        return latex_section;
    }

    public void setLatex_section(latex_Section latex_section) {
        this.latex_section = latex_section;
    }

}