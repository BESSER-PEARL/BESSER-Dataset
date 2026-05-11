





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_DiagnosticParam  {

    private String copyToVar;
    private String qualifier;





    private DiagonosticModel_DiagnosticRequest diagonosticmodel_diagnosticrequest;




    private DiagonosticModel_DiagnosticResponse diagonosticmodel_diagnosticresponse;


    public DiagonosticModel_DiagnosticParam(
        String copyToVar,        String qualifier    ) {
        this.copyToVar = copyToVar;
        this.qualifier = qualifier;
    }


    public String getCopytovar() {
        return copyToVar;
    }

    public void setCopytovar(String copyToVar) {
        this.copyToVar = copyToVar;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }

    public DiagonosticModel_DiagnosticRequest getDiagonosticmodel_diagnosticrequest() {
        return diagonosticmodel_diagnosticrequest;
    }

    public void setDiagonosticmodel_diagnosticrequest(DiagonosticModel_DiagnosticRequest diagonosticmodel_diagnosticrequest) {
        this.diagonosticmodel_diagnosticrequest = diagonosticmodel_diagnosticrequest;
    }
    public DiagonosticModel_DiagnosticResponse getDiagonosticmodel_diagnosticresponse() {
        return diagonosticmodel_diagnosticresponse;
    }

    public void setDiagonosticmodel_diagnosticresponse(DiagonosticModel_DiagnosticResponse diagonosticmodel_diagnosticresponse) {
        this.diagonosticmodel_diagnosticresponse = diagonosticmodel_diagnosticresponse;
    }

}