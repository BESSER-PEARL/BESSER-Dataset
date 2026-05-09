





import java.util.List;
import java.util.ArrayList;

public class miniOCL_PathNameCS  {






    private miniOCL_ConstraintCS miniocl_constraintcs;




    private List<miniOCL_PathElementCS> miniocl_pathelementcss;




    private miniOCL_ClassCS miniocl_classcs;




    private miniOCL_NameExpCS miniocl_nameexpcs;




    private miniOCL_ParameterCS miniocl_parametercs;


    public miniOCL_PathNameCS(
    ) {
        this.miniocl_pathelementcss = new ArrayList<>();
    }

    public miniOCL_PathNameCS(
        ArrayList<miniOCL_PathElementCS> miniocl_pathelementcss    ) {
        this.miniocl_pathelementcss = miniocl_pathelementcss;
    }


    public miniOCL_ConstraintCS getMiniocl_constraintcs() {
        return miniocl_constraintcs;
    }

    public void setMiniocl_constraintcs(miniOCL_ConstraintCS miniocl_constraintcs) {
        this.miniocl_constraintcs = miniocl_constraintcs;
    }
    public List<miniOCL_PathElementCS> getMiniocl_pathelementcss() {
        return miniocl_pathelementcss;
    }

    public void addMiniocl_pathelementcs(Miniocl_pathelementcs miniocl_pathelementcs) {
        this.miniocl_pathelementcss.add(miniocl_pathelementcs);
    }
    public miniOCL_ClassCS getMiniocl_classcs() {
        return miniocl_classcs;
    }

    public void setMiniocl_classcs(miniOCL_ClassCS miniocl_classcs) {
        this.miniocl_classcs = miniocl_classcs;
    }
    public miniOCL_NameExpCS getMiniocl_nameexpcs() {
        return miniocl_nameexpcs;
    }

    public void setMiniocl_nameexpcs(miniOCL_NameExpCS miniocl_nameexpcs) {
        this.miniocl_nameexpcs = miniocl_nameexpcs;
    }
    public miniOCL_ParameterCS getMiniocl_parametercs() {
        return miniocl_parametercs;
    }

    public void setMiniocl_parametercs(miniOCL_ParameterCS miniocl_parametercs) {
        this.miniocl_parametercs = miniocl_parametercs;
    }

}