





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ClassBody  {






    private List<javaDsl_ClassBodyDeclaration> javadsl_classbodydeclarations;




    private javaDsl_ClassDeclaration javadsl_classdeclaration;


    public javaDsl_ClassBody(
    ) {
        this.javadsl_classbodydeclarations = new ArrayList<>();
    }

    public javaDsl_ClassBody(
        ArrayList<javaDsl_ClassBodyDeclaration> javadsl_classbodydeclarations    ) {
        this.javadsl_classbodydeclarations = javadsl_classbodydeclarations;
    }


    public List<javaDsl_ClassBodyDeclaration> getJavadsl_classbodydeclarations() {
        return javadsl_classbodydeclarations;
    }

    public void addJavadsl_classbodydeclaration(Javadsl_classbodydeclaration javadsl_classbodydeclaration) {
        this.javadsl_classbodydeclarations.add(javadsl_classbodydeclaration);
    }
    public javaDsl_ClassDeclaration getJavadsl_classdeclaration() {
        return javadsl_classdeclaration;
    }

    public void setJavadsl_classdeclaration(javaDsl_ClassDeclaration javadsl_classdeclaration) {
        this.javadsl_classdeclaration = javadsl_classdeclaration;
    }

}