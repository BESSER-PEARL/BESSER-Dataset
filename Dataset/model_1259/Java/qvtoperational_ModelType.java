





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_ModelType extends Class {

    private String conformanceKind;





    private List<qvtoperational_OCLExpression> qvtoperational_oclexpressions;




    private List<qvtoperational_Package> qvtoperational_packages;


    public qvtoperational_ModelType(
        String conformanceKind    ) {
        super(
        );
        this.conformanceKind = conformanceKind;
        this.qvtoperational_oclexpressions = new ArrayList<>();
        this.qvtoperational_packages = new ArrayList<>();
    }

    public qvtoperational_ModelType(
        String conformanceKind        ArrayList<qvtoperational_OCLExpression> qvtoperational_oclexpressions,        ArrayList<qvtoperational_Package> qvtoperational_packages    ) {
        this.conformanceKind = conformanceKind;
        this.qvtoperational_oclexpressions = qvtoperational_oclexpressions;
        this.qvtoperational_packages = qvtoperational_packages;
    }

    public String getConformancekind() {
        return conformanceKind;
    }

    public void setConformancekind(String conformanceKind) {
        this.conformanceKind = conformanceKind;
    }

    public List<qvtoperational_OCLExpression> getQvtoperational_oclexpressions() {
        return qvtoperational_oclexpressions;
    }

    public void addQvtoperational_oclexpression(Qvtoperational_oclexpression qvtoperational_oclexpression) {
        this.qvtoperational_oclexpressions.add(qvtoperational_oclexpression);
    }
    public List<qvtoperational_Package> getQvtoperational_packages() {
        return qvtoperational_packages;
    }

    public void addQvtoperational_package(Qvtoperational_package qvtoperational_package) {
        this.qvtoperational_packages.add(qvtoperational_package);
    }

}