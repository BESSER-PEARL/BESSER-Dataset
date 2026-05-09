





import java.util.List;
import java.util.ArrayList;

public class classifiers_ConcreteClassifier extends MemberContainer, AnnotableAndModifiable, Member, Statement, Classifier, TypeParametrizable {

    private String fullName;



    public classifiers_ConcreteClassifier(
        String fullName    ) {
        super(
        );
        this.fullName = fullName;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }


}