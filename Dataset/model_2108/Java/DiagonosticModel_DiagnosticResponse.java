





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_DiagnosticResponse  {

    private String primitive;





    private DiagonosticModel_DiagnosticService diagonosticmodel_diagnosticservice;


    public DiagonosticModel_DiagnosticResponse(
        String primitive    ) {
        this.primitive = primitive;
    }


    public String getPrimitive() {
        return primitive;
    }

    public void setPrimitive(String primitive) {
        this.primitive = primitive;
    }

    public DiagonosticModel_DiagnosticService getDiagonosticmodel_diagnosticservice() {
        return diagonosticmodel_diagnosticservice;
    }

    public void setDiagonosticmodel_diagnosticservice(DiagonosticModel_DiagnosticService diagonosticmodel_diagnosticservice) {
        this.diagonosticmodel_diagnosticservice = diagonosticmodel_diagnosticservice;
    }

}