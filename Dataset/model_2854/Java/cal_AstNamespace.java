





import java.util.List;
import java.util.ArrayList;

public class cal_AstNamespace extends AstPackage, AstTop, AstUnit {

    private String name;





    private List<cal_AstNamespace> cal_astnamespaces;


    public cal_AstNamespace(
        String name    ) {
        super(
        );
        this.name = name;
        this.cal_astnamespaces = new ArrayList<>();
    }

    public cal_AstNamespace(
        String name        ArrayList<cal_AstNamespace> cal_astnamespaces    ) {
        this.name = name;
        this.cal_astnamespaces = cal_astnamespaces;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<cal_AstNamespace> getCal_astnamespaces() {
        return cal_astnamespaces;
    }

    public void addCal_astnamespace(Cal_astnamespace cal_astnamespace) {
        this.cal_astnamespaces.add(cal_astnamespace);
    }

}