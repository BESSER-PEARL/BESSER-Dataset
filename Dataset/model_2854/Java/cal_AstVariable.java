





import java.util.List;
import java.util.ArrayList;

public class cal_AstVariable  {

    private String name;
    private boolean constant;





    private cal_AstFunction cal_astfunction;




    private cal_AstFunction cal_astfunction;




    private cal_AstNamespace cal_astnamespace;




    private cal_AstFunction cal_astfunction;


    public cal_AstVariable(
        String name,        boolean constant    ) {
        this.name = name;
        this.constant = constant;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }

    public cal_AstFunction getCal_astfunction() {
        return cal_astfunction;
    }

    public void setCal_astfunction(cal_AstFunction cal_astfunction) {
        this.cal_astfunction = cal_astfunction;
    }
    public cal_AstFunction getCal_astfunction() {
        return cal_astfunction;
    }

    public void setCal_astfunction(cal_AstFunction cal_astfunction) {
        this.cal_astfunction = cal_astfunction;
    }
    public cal_AstNamespace getCal_astnamespace() {
        return cal_astnamespace;
    }

    public void setCal_astnamespace(cal_AstNamespace cal_astnamespace) {
        this.cal_astnamespace = cal_astnamespace;
    }
    public cal_AstFunction getCal_astfunction() {
        return cal_astfunction;
    }

    public void setCal_astfunction(cal_AstFunction cal_astfunction) {
        this.cal_astfunction = cal_astfunction;
    }

}