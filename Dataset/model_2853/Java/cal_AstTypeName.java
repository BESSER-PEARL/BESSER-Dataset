





import java.util.List;
import java.util.ArrayList;

public class cal_AstTypeName  {

    private String name;





    private cal_AstNamespace cal_astnamespace;




    private List<cal_AstFunction> cal_astfunctions;


    public cal_AstTypeName(
        String name    ) {
        this.name = name;
        this.cal_astfunctions = new ArrayList<>();
    }

    public cal_AstTypeName(
        String name        ArrayList<cal_AstFunction> cal_astfunctions    ) {
        this.name = name;
        this.cal_astfunctions = cal_astfunctions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstNamespace getCal_astnamespace() {
        return cal_astnamespace;
    }

    public void setCal_astnamespace(cal_AstNamespace cal_astnamespace) {
        this.cal_astnamespace = cal_astnamespace;
    }
    public List<cal_AstFunction> getCal_astfunctions() {
        return cal_astfunctions;
    }

    public void addCal_astfunction(Cal_astfunction cal_astfunction) {
        this.cal_astfunctions.add(cal_astfunction);
    }

}