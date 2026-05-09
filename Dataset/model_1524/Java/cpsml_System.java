





import java.util.List;
import java.util.ArrayList;

public class cpsml_System  {

    private int sub;
    private String ran;
    private String name;
    private int y0label;





    private List<cpsml_Variable> cpsml_variables;




    private cpsml_Variable cpsml_variable;


    public cpsml_System(
        int sub,        String ran,        String name,        int y0label    ) {
        this.sub = sub;
        this.ran = ran;
        this.name = name;
        this.y0label = y0label;
        this.cpsml_variables = new ArrayList<>();
    }

    public cpsml_System(
        int sub,        String ran,        String name,        int y0label        ArrayList<cpsml_Variable> cpsml_variables    ) {
        this.sub = sub;
        this.ran = ran;
        this.name = name;
        this.y0label = y0label;
        this.cpsml_variables = cpsml_variables;
    }

    public int getSub() {
        return sub;
    }

    public void setSub(int sub) {
        this.sub = sub;
    }
    public String getRan() {
        return ran;
    }

    public void setRan(String ran) {
        this.ran = ran;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getY0label() {
        return y0label;
    }

    public void setY0label(int y0label) {
        this.y0label = y0label;
    }

    public List<cpsml_Variable> getCpsml_variables() {
        return cpsml_variables;
    }

    public void addCpsml_variable(Cpsml_variable cpsml_variable) {
        this.cpsml_variables.add(cpsml_variable);
    }
    public cpsml_Variable getCpsml_variable() {
        return cpsml_variable;
    }

    public void setCpsml_variable(cpsml_Variable cpsml_variable) {
        this.cpsml_variable = cpsml_variable;
    }

}