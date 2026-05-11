





import java.util.List;
import java.util.ArrayList;

public class aDSL_Method extends Member {

    private String name;
    private boolean isconst;
    private boolean istyped;





    private aDSL_VariableType adsl_variabletype;




    private List<aDSL_Parameter> adsl_parameters;


    public aDSL_Method(
        String name,        boolean isconst,        boolean istyped    ) {
        super(
        );
        this.name = name;
        this.isconst = isconst;
        this.istyped = istyped;
        this.adsl_parameters = new ArrayList<>();
    }

    public aDSL_Method(
        String name,        boolean isconst,        boolean istyped        ArrayList<aDSL_Parameter> adsl_parameters    ) {
        this.name = name;
        this.isconst = isconst;
        this.istyped = istyped;
        this.adsl_parameters = adsl_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsconst() {
        return isconst;
    }

    public void setIsconst(boolean isconst) {
        this.isconst = isconst;
    }
    public boolean getIstyped() {
        return istyped;
    }

    public void setIstyped(boolean istyped) {
        this.istyped = istyped;
    }

    public aDSL_VariableType getAdsl_variabletype() {
        return adsl_variabletype;
    }

    public void setAdsl_variabletype(aDSL_VariableType adsl_variabletype) {
        this.adsl_variabletype = adsl_variabletype;
    }
    public List<aDSL_Parameter> getAdsl_parameters() {
        return adsl_parameters;
    }

    public void addAdsl_parameter(Adsl_parameter adsl_parameter) {
        this.adsl_parameters.add(adsl_parameter);
    }

}