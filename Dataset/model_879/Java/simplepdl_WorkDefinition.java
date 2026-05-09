





import java.util.List;
import java.util.ArrayList;

public class simplepdl_WorkDefinition extends Activities {






    private simplepdl_ParameterWD simplepdl_parameterwd;




    private List<simplepdl_ParameterWD> simplepdl_parameterwds;


    public simplepdl_WorkDefinition(
    ) {
        super(
        );
        this.simplepdl_parameterwds = new ArrayList<>();
    }

    public simplepdl_WorkDefinition(
        ArrayList<simplepdl_ParameterWD> simplepdl_parameterwds    ) {
        this.simplepdl_parameterwds = simplepdl_parameterwds;
    }


    public simplepdl_ParameterWD getSimplepdl_parameterwd() {
        return simplepdl_parameterwd;
    }

    public void setSimplepdl_parameterwd(simplepdl_ParameterWD simplepdl_parameterwd) {
        this.simplepdl_parameterwd = simplepdl_parameterwd;
    }
    public List<simplepdl_ParameterWD> getSimplepdl_parameterwds() {
        return simplepdl_parameterwds;
    }

    public void addSimplepdl_parameterwd(Simplepdl_parameterwd simplepdl_parameterwd) {
        this.simplepdl_parameterwds.add(simplepdl_parameterwd);
    }

}