





import java.util.List;
import java.util.ArrayList;

public class cal_AstFunction extends AstExternalFunction {

    private String name;





    private cal_AstNamespace cal_astnamespace;


    public cal_AstFunction(
        String name    ) {
        super(
        );
        this.name = name;
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

}