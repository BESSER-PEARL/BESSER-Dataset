





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_Var extends DiagnosticParamValueType {

    private String name;



    public DiagonosticModel_Var(
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


}