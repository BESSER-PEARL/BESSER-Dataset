





import java.util.List;
import java.util.ArrayList;

public class UsecaseDSL_Classifier extends Namespace {






    private UsecaseDSL_UseCase usecasedsl_usecase;




    private UsecaseDSL_Association_c usecasedsl_association_c;




    private List<UsecaseDSL_Classifier> usecasedsl_classifiers;




    private UsecaseDSL_Association_c usecasedsl_association_c;




    private UsecaseDSL_UseCaseDiagram_c usecasedsl_usecasediagram_c;




    private UsecaseDSL_Generalization usecasedsl_generalization;




    private UsecaseDSL_Generalization usecasedsl_generalization;




    private List<UsecaseDSL_Generalization> usecasedsl_generalizations;




    private UsecaseDSL_System_c usecasedsl_system_c;


    public UsecaseDSL_Classifier(
    ) {
        super(
        );
        this.usecasedsl_classifiers = new ArrayList<>();
        this.usecasedsl_generalizations = new ArrayList<>();
    }

    public UsecaseDSL_Classifier(
        ArrayList<UsecaseDSL_Classifier> usecasedsl_classifiers,        ArrayList<UsecaseDSL_Generalization> usecasedsl_generalizations    ) {
        this.usecasedsl_classifiers = usecasedsl_classifiers;
        this.usecasedsl_generalizations = usecasedsl_generalizations;
    }


    public UsecaseDSL_UseCase getUsecasedsl_usecase() {
        return usecasedsl_usecase;
    }

    public void setUsecasedsl_usecase(UsecaseDSL_UseCase usecasedsl_usecase) {
        this.usecasedsl_usecase = usecasedsl_usecase;
    }
    public UsecaseDSL_Association_c getUsecasedsl_association_c() {
        return usecasedsl_association_c;
    }

    public void setUsecasedsl_association_c(UsecaseDSL_Association_c usecasedsl_association_c) {
        this.usecasedsl_association_c = usecasedsl_association_c;
    }
    public List<UsecaseDSL_Classifier> getUsecasedsl_classifiers() {
        return usecasedsl_classifiers;
    }

    public void addUsecasedsl_classifier(Usecasedsl_classifier usecasedsl_classifier) {
        this.usecasedsl_classifiers.add(usecasedsl_classifier);
    }
    public UsecaseDSL_Association_c getUsecasedsl_association_c() {
        return usecasedsl_association_c;
    }

    public void setUsecasedsl_association_c(UsecaseDSL_Association_c usecasedsl_association_c) {
        this.usecasedsl_association_c = usecasedsl_association_c;
    }
    public UsecaseDSL_UseCaseDiagram_c getUsecasedsl_usecasediagram_c() {
        return usecasedsl_usecasediagram_c;
    }

    public void setUsecasedsl_usecasediagram_c(UsecaseDSL_UseCaseDiagram_c usecasedsl_usecasediagram_c) {
        this.usecasedsl_usecasediagram_c = usecasedsl_usecasediagram_c;
    }
    public UsecaseDSL_Generalization getUsecasedsl_generalization() {
        return usecasedsl_generalization;
    }

    public void setUsecasedsl_generalization(UsecaseDSL_Generalization usecasedsl_generalization) {
        this.usecasedsl_generalization = usecasedsl_generalization;
    }
    public UsecaseDSL_Generalization getUsecasedsl_generalization() {
        return usecasedsl_generalization;
    }

    public void setUsecasedsl_generalization(UsecaseDSL_Generalization usecasedsl_generalization) {
        this.usecasedsl_generalization = usecasedsl_generalization;
    }
    public List<UsecaseDSL_Generalization> getUsecasedsl_generalizations() {
        return usecasedsl_generalizations;
    }

    public void addUsecasedsl_generalization(Usecasedsl_generalization usecasedsl_generalization) {
        this.usecasedsl_generalizations.add(usecasedsl_generalization);
    }
    public UsecaseDSL_System_c getUsecasedsl_system_c() {
        return usecasedsl_system_c;
    }

    public void setUsecasedsl_system_c(UsecaseDSL_System_c usecasedsl_system_c) {
        this.usecasedsl_system_c = usecasedsl_system_c;
    }

}