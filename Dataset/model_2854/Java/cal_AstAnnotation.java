





import java.util.List;
import java.util.ArrayList;

public class cal_AstAnnotation  {

    private String name;





    private cal_AstEntity cal_astentity;




    private cal_AstVariable cal_astvariable;




    private cal_AstFunction cal_astfunction;




    private cal_AstNamespace cal_astnamespace;


    public cal_AstAnnotation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstEntity getCal_astentity() {
        return cal_astentity;
    }

    public void setCal_astentity(cal_AstEntity cal_astentity) {
        this.cal_astentity = cal_astentity;
    }
    public cal_AstVariable getCal_astvariable() {
        return cal_astvariable;
    }

    public void setCal_astvariable(cal_AstVariable cal_astvariable) {
        this.cal_astvariable = cal_astvariable;
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

}