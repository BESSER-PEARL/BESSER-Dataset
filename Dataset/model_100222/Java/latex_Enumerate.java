





import java.util.List;
import java.util.ArrayList;

public class latex_Enumerate  {

    private String enumprefix;
    private String enumtext;





    private List<latex_General> latex_generals;




    private latex_Body latex_body;


    public latex_Enumerate(
        String enumprefix,        String enumtext    ) {
        this.enumprefix = enumprefix;
        this.enumtext = enumtext;
        this.latex_generals = new ArrayList<>();
    }

    public latex_Enumerate(
        String enumprefix,        String enumtext        ArrayList<latex_General> latex_generals    ) {
        this.enumprefix = enumprefix;
        this.enumtext = enumtext;
        this.latex_generals = latex_generals;
    }

    public String getEnumprefix() {
        return enumprefix;
    }

    public void setEnumprefix(String enumprefix) {
        this.enumprefix = enumprefix;
    }
    public String getEnumtext() {
        return enumtext;
    }

    public void setEnumtext(String enumtext) {
        this.enumtext = enumtext;
    }

    public List<latex_General> getLatex_generals() {
        return latex_generals;
    }

    public void addLatex_general(Latex_general latex_general) {
        this.latex_generals.add(latex_general);
    }
    public latex_Body getLatex_body() {
        return latex_body;
    }

    public void setLatex_body(latex_Body latex_body) {
        this.latex_body = latex_body;
    }

}