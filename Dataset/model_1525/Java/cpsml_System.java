





import java.util.List;
import java.util.ArrayList;

public class cpsml_System  {

    private int sub;
    private String name;
    private String ran;
    private int y0label;





    private List<cpsml_ODE> cpsml_odes;


    public cpsml_System(
        int sub,        String name,        String ran,        int y0label    ) {
        this.sub = sub;
        this.name = name;
        this.ran = ran;
        this.y0label = y0label;
        this.cpsml_odes = new ArrayList<>();
    }

    public cpsml_System(
        int sub,        String name,        String ran,        int y0label        ArrayList<cpsml_ODE> cpsml_odes    ) {
        this.sub = sub;
        this.name = name;
        this.ran = ran;
        this.y0label = y0label;
        this.cpsml_odes = cpsml_odes;
    }

    public int getSub() {
        return sub;
    }

    public void setSub(int sub) {
        this.sub = sub;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRan() {
        return ran;
    }

    public void setRan(String ran) {
        this.ran = ran;
    }
    public int getY0label() {
        return y0label;
    }

    public void setY0label(int y0label) {
        this.y0label = y0label;
    }

    public List<cpsml_ODE> getCpsml_odes() {
        return cpsml_odes;
    }

    public void addCpsml_ode(Cpsml_ode cpsml_ode) {
        this.cpsml_odes.add(cpsml_ode);
    }

}